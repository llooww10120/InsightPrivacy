# InsightPrivacy
透過Line Bot 將網址透過 NLP 語意分析得到相對簡短的隱私條款

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
### model
[UsageTest_model](https://drive.google.com/drive/u/0/folders/1-4fiUJ98LI-fe_7OVm3Qsu0pDLPO2mTO)

## output


