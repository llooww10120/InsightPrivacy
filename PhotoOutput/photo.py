#main.py
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image

#output
def DrawPic(draw, font, output_list):
    
    Array_Row_Number = len(output_list)

    InsightPrivacy = "InsightPrivacy "
    draw.text((350, 50), InsightPrivacy, font=font, align="right", fill=(41,36,33), size=1000)
    
    x = 10
    y = 120
    for index_r in range(0,Array_Row_Number):
        Array_Column_Number = len(output_list[index_r])
        x = 10
        y = y + 100
        for index_c in range(0,Array_Column_Number):
            draw.multiline_text((x, y), output_list[index_r][index_c], fill=(128,128,105), font=font,align='center')
            x += 200
            
        return








def CreatePic():

    output_list = [
        ['聯絡資訊', '住址', '工作地址', '以前地址', '住家電話號碼', '行動電話', '即時通帳號'],
        ['姓名', '生日', '名字'],
        ['身分證號', '統一編號', '身分證統一編號', '統一證號', '稅籍編號', '保險憑證號碼',
            '殘障手冊號碼', '退休證之號碼', '證照號碼', '護照號碼', '身分證字號'],
        ['瀏覽資訊 IP 位址', '設備資訊', '藍芽聯絡人', '郵遞區號', '手機製造商', '手機型號', 'UDID']
    ]
    
    #創建背景
    img = np.zeros((450, 450, 3), np.uint8) #黑背景
    cv2img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #如果是cv2讀取圖片才需
    cv2img[:] = (255,255,240) # 上色
    cv2img = cv2.resize(cv2img, (2000, 1000))
    
    # 將numpy陣列轉換為PIL影像
    imgPil = Image.fromarray(cv2img)
    
    #在圖片上加入文字
    draw = ImageDraw.Draw(imgPil)
    font = ImageFont.truetype('SimHei.ttf', 20, encoding='utf-8')
    DrawPic(draw, font, output_list)

    #將PIL轉回Numpy陣列
    cv2charimg = cv2.cvtColor(np.array(imgPil), cv2.COLOR_RGB2BGR)
    # cv2img = np.array(imgPil)

    #呈現在螢幕上,除錯
    cv2.imshow('Ouput', cv2charimg)
    cv2.waitKey(0)

    #輸出圖片檔
    cv2.imwrite('Output.jpg', cv2charimg)

#避免引用檔案時
if __name__== "__main__":
    CreatePic()
