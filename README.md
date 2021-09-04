# InsightPrivacy
使用者將隱私權網址傳給 Line Bot ，並使用 BERT 技術透過 NLP 語意分析得到簡潔的隱私條款。
![](https://i.imgur.com/6PXos9R.png)

## 內容
在這份 README 中，InsightPrivacy 分別使用以下之檔案，並在此作依序概述，詳細於後方中描述。

1. `car.py` : 這段程式碼執行爬蟲，將網址內的隱私權條款抓取進而做後續處理。
2. `data_processing.py` : 這段程式碼執行資料預處理，將雜訊做處理，並提找出相應關鍵字。
3. `bert.ipynb` : 這段程式碼執行Bert模型的訓練，本專案之核心，用於隱私權之預測。
4. `UsageTest.py` : 這段程式碼執行為以訓練好的模型預測用，將預測文字輸入得到結果。
5. `photo.py` :   這段程式碼執行提取data_processing之資料後處理為更好閱讀之圖片輸出，方便line使用者觀看。
6. `main.py` : 這段程式碼執行為將前面模型資料輸出並配合原本的條款，做成文字圖片輸出，方便line使用者觀看。
7. `CreatImage.py` : 這段程式碼將使用著傳入的訊息，傳入爬蟲程式，再將回傳的內容送入模型中，最後使用上面的程式製造圖片，並使用Imgur api自動上傳至圖床。
8. `Upload2Imgur.py` : 上傳圖片及獲取圖片網址。
## 安裝需求
本專案使用Python語言，並搭配以下安裝使用。

>Flask == 2.0.1
gunicorn == 20.1.0
line-bot-sdk == 1.19.0 
beautifulsoup4 == 4.9.3
requests == 2.24.0
tqdm == 4.47.0
Pillow == 8.3.1
Pillow-PIL == 0.1.dev0
numpy == 1.21.1
opencv-python == 4.5.3.56
configparser == 5.0.0
pandas == 1.1.5
torch == 1.9.0+cu102
transformers == 4.9.2



## 爬蟲`car.py`
| Name | Input型別 | Output型別 |
|:----:|:---------:|:----------:|
| cra  |  string   |  list(1d)  |

輸入給予網址進行爬蟲，並符合以下規則。

- 遇到`。`做換行。
- 先用`<p>`做爬蟲，如果小於700字則爬全文(由於隱私權經大數據分析，若需符合基本規格會大於1000字，則用此規則排除雜訊)。
- 濾掉`單一空格行`、`換行`、`\r`、`\t` 等資料雜訊。

新增到list中，以換行為一單位，並回傳其值。

## 資料預處理`data_processing.py`
|      Name       | Input型別 | Output型別 |
|:---------------:|:---------:|:----------:|
| data_processing | list(1d)  |  list(2d)  |

從`cra.py`中獲取list，並做關鍵字預處理。

用2D-list搭配以篩選過的表做記數，回傳大於1的關鍵字list。

## NLP模型訓練`bert.ipynb`
- pytorch 1.9.0+cu111
### BERT
BERT(Bidirectional Encoder Representations from Transformers)由這個名字就可以得知，這個模型的架構就是另一個模型Transformer的Encoder，2018年由Google推出，推出後半年左右各大排行榜上都可以看到這個模型的名字，BERT可以達成許多不同的任務，如單一或成對的句子分類、句子的標註、利用問題與文章達成的簡答問題等，在使用上我們也只需要少量的資料就可以讓模型擁有不錯的準確率
![](https://i.imgur.com/qiswWqU.png)
### Fine-Tuning
Bert在使用上可以不用把模型從頭開始訓練，我們可以用Fine-Tuning的方式，將以經訓練好的模型，利用我們擁有的資料對模型做微調來達到我們要的功能，利用這種方式可以開發更加快速，也可以用較少的資料達到更好的結果
在這一次的計畫中我們使用了HuggingFace的transformers資料庫中的預訓練模型來進行
![](https://i.imgur.com/QTNVDr6.jpg)
### 目前訓練結果
我們目前所擁有的資料較為稀少，因此我們決定先將手邊所擁有的資料用於訓練，並觀察訓練出來的模型的表現
訓練過後最後訓練資料的準確率來到了97.5%，在備標住起來的87個句子中，只有兩句被判別錯誤，其中1句為全英文的句子，而另一句子經過我們的判別後，認為它其實不應該被標註起來。在觀察模型所做的標註後發現此模型也標出了許多判定起來很微妙的句子
以google的隱私條款為例
![](https://i.imgur.com/uWvvh4i.jpg)
![](https://i.imgur.com/18DqtYs.jpg)
![](https://i.imgur.com/MuuYPrA.jpg)
![](https://i.imgur.com/cHUt46h.jpg)
![](https://i.imgur.com/kuKQavW.jpg)
![](https://i.imgur.com/LXeEkzN.jpg)
有些句子甚至被標記起來也不意外
因此我們認為目前以我們的資料量能達到這樣的成果是超乎預期的



## NLP結果預測`UsageTest.py`
|Name | Input | Output |
| -------- | -------- | -------- |
| usagetest(text) |  list(2d)  | list(1d)  |

輸入為字串形成的list
 
輸出為1與0形成的list 對應輸入的每一個句子

使用時要將.bth檔的model放到此資料夾
### model
[UsageTest_model](https://drive.google.com/drive/u/0/folders/1-4fiUJ98LI-fe_7OVm3Qsu0pDLPO2mTO)


## 圖片輸出`photo.py` & `main.py`
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| PhotoOutput | list(2d)| png    |
| FinalOutputInApp | list(1d), list(1d)| jpg |

- **PhotoOutput `main.py`** 
從data_processing中獲取list。
使文字轉為圖片儲存。

- **FinalOutputInApp `photo.py`**
從model得到的list與原model處理前的資料處理後得到了圖片
其中圖片使用了opencv與pillow和numpy套件
使文字輸出到圖形圖片後呈現給客戶端看

## CreatOutput
### `Upload2Imgur.py`
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| upload2imgur| string      | string    |
- 給予圖片位址上傳至Imgur圖床，並回傳網址

| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| getimg      | string      | string    |
- 給予image_name回傳圖片網址
## `CreatImage.py`
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| ImageOutput | string      | list(1d)    |
- 給予event.message.text轉換成2張圖片後自動上傳至Imgur圖床，並回傳網址
## 未來展望
1.多重目的的模型訓練
    獲取更多資料量，進行多標籤的模型訓練。
2.法條比對的model
    可能將會繼續以 bert 模型進行語意分析，判斷是否有不適合的地方。
