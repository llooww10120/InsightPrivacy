import torch
from transformers import BertTokenizer
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from transformers import BertForSequenceClassification

#pytorch的dataset 用來將資料轉成bert讀得懂的格式
class ClauseDataset(Dataset):
    def __init__(self,text,tokenizer,label=None):
        self.text=text
        self.label=label
        self.tokenizer=tokenizer
        self.len=len(self.text)
    def __getitem__(self,idx):
        tokens=self.tokenizer(self.text[idx],padding=True,truncation=True,max_length=512)
        ids=tokens["input_ids"]
        segments=tokens["token_type_ids"]
        masks =tokens["attention_mask"]
        tokens_tensor=torch.tensor(ids)
        segments_tensor=torch.tensor(segments)
        masks_tensors=torch.tensor(masks)
        if self.label:
            label_tensor=torch.tensor(self.label[idx])
        else:
            label_tensor=None
        return(tokens_tensor, segments_tensor, masks_tensors, label_tensor)
    def __len__(self):
        return self.len

#用在dataloader的函式
def create_mini_batch(samples):
    tokens_tensors = [s[0] for s in samples]
    segments_tensors = [s[1] for s in samples]
    masks_tensors =[s[2] for s in samples]
    if samples[0][3] is not None:
        label_ids = torch.stack([s[3] for s in samples])
    else:
        label_ids = None
    tokens_tensors = pad_sequence(tokens_tensors,batch_first=True)
    segments_tensors = pad_sequence(segments_tensors,batch_first=True)
    masks_tensors = pad_sequence(masks_tensors,batch_first=True)

    return tokens_tensors, segments_tensors, masks_tensors, label_ids

#預測函式
def get_predictions(model, dataloader, compute_acc=False):
    predictions = None
    correct = 0
    total = 0
      
    with torch.no_grad():
        # 遍巡整個資料集
        for data in dataloader:
            # 將所有 tensors 移到 GPU 上
            if next(model.parameters()).is_cuda:
                data = [t.to("cuda:0") for t in data if t is not None]
            # 別忘記前 3 個 tensors 分別為 tokens, segments 以及 masks
            # 且強烈建議在將這些 tensors 丟入 `model` 時指定對應的參數名稱
            tokens_tensors, segments_tensors, masks_tensors = data[:3]
            outputs = model(input_ids=tokens_tensors, 
                            token_type_ids=segments_tensors, 
                            attention_mask=masks_tensors)
            
            logits = outputs[0]
            _, pred = torch.max(logits.data, 1)
            
            # 用來計算訓練集的分類準確率
            if compute_acc:
                labels = data[3]
                total += labels.size(0)
                correct += (pred == labels).sum().item()
                
            # 將當前 batch 記錄下來
            if predictions is None:
                predictions = pred
            else:
                predictions = torch.cat((predictions, pred))
    
    if compute_acc:
        acc = correct / total
        return predictions, acc
    return predictions
#給其他程式呼叫的函式
def usagetest(text):
    
    PRETRAINED_MODEL_NAME = "bert-base-chinese"

    NUM_LABELS = 2
    model = BertForSequenceClassification.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("device:", device)
    model = model.to(device)
    #path為model所放的位置
    PATH=r"UsageTest\bert20210821.pth"
    #因為gpu不可用時會出錯 因此加上後面的參數強制用cpu跑
    checkpoint = torch.load(PATH,map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint)


    model.eval()
    PRETRAINED_MODEL_NAME = "bert-base-chinese"
    tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
    testset=ClauseDataset(text,tokenizer=tokenizer)
    BATCH_SIZE = 8
    testloader = DataLoader(testset, batch_size=BATCH_SIZE, collate_fn=create_mini_batch)
    predictions = get_predictions(model, testloader)
    return predictions.tolist()

if __name__=="__main__":
    text1=["您的資料將用於網站的維護及改善","我們將不會隨意刪除您的資料"]
    pre=usagetest(text1)
    print(pre)