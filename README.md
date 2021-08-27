# InsightPrivacy
使用者將隱私權網址傳給 Line Bot ，並使用 BERT 技術透過 NLP 語意分析得到簡潔的隱私條款。

## 內容
在這份 README 中，InsightPrivacy 

## CreatOutput
### CreatImage
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| ImageOutput | string      | list(1d)    |
- 給予event.message.text轉換成2張圖片後自動上傳至Imgur圖床，並回傳網址
### Upload2Imgur
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| upload2imgur| string      | string    |
- 給予圖片位址上傳至Imgur圖床，並回傳網址

| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| getimg      | string      | string    |
- 給予image_name回傳圖片網址
## crawler
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| cra         | string      | list(1d)    |

給予url進行爬蟲，並符合以下規則。

- 遇到`。`做換行。
- 先用`<p>`做爬蟲，如果小於700字則爬全文。
- 濾掉`單一空格行`、`換行`、`\r`、`\t` 等渣渣。

新增到list中，以換行為一單位，並return。

## data processing
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| data_processing | list(1d)| list(2d)    |

從cra中獲取list，並做關鍵字預處理。

用2D-list搭配table做記數，return大於1的關鍵字table。

## NLP
- pytorch 1.9.0+cu111
## UsageTest
|Name | Input | Output |
| -------- | -------- | -------- |
| usagetest(text) |  list(2d)  | list(1d)  |

輸入為字串形成的list
 
輸出為1與0形成的list 對應輸入的每一個句子

使用時要將.bth檔的model放到此資料夾
### model
[UsageTest_model](https://drive.google.com/drive/u/0/folders/1-4fiUJ98LI-fe_7OVm3Qsu0pDLPO2mTO)

## Output
| Name        | Input型別   | Output型別  |
| :-----------: |:-----------:| :-----------:|
| PhotoOutput | list(2d)| png    |
| FinalOutputInApp | list(1d), list(1d)| jpg |

-PhotoOutput
從data_processing中獲取list。

使文字轉為圖片儲存。

-FinalOutputInApp
從model得到的list與原model處理前的資料處理後得到了圖片

使文字輸出到圖形圖片後呈現給客戶端看

