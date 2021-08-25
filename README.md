# InsightPrivacy
## LINE BOT

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

### model
[UsageTest_model](https://drive.google.com/drive/u/0/folders/1-4fiUJ98LI-fe_7OVm3Qsu0pDLPO2mTO)

## output


