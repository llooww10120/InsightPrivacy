import pandas as pd
import torch
from transformers import BertTokenizer
from IPython.display import clear_output
from transformers import BertForSequenceClassification


def usagetest(text,model):
    model.eval()
    predictions = None
    tokens=tokenizer(text,padding=True,truncation=True,max_length=512)
    ids=tokens["input_ids"]
    segments=tokens["token_type_ids"]
    masks =tokens["attention_mask"]
    tokens_tensor=torch.tensor([ids])
    segments_tensor=torch.tensor([segments])
    masks_tensors=torch.tensor([masks])
    outputs = model(input_ids=tokens_tensor, token_type_ids=segments_tensor, attention_mask=masks_tensors)
    logits = outputs[0]
    _, pred = torch.max(logits.data, 1)
    return pred
if __name__=="__main__":
    PRETRAINED_MODEL_NAME = "bert-base-chinese"
    tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
    NUM_LABELS = 2
    model = BertForSequenceClassification.from_pretrained(PRETRAINED_MODEL_NAME, num_labels=NUM_LABELS)
    clear_output()

    PATH="bert20210821.pth"
    checkpoint = torch.load(PATH,map_location=torch.device('cpu'))
    model.load_state_dict(checkpoint)

    text="您的資料將用於網站的維護及改善"
    pred1 = usagetest(text,model)
    text2 ="我們將不會隨意刪除您的資料"
    pred2 = usagetest(text2,model)
    print(f"""
        text1:{int(pred1)}
        text2:{int(pred2)}
        """)
