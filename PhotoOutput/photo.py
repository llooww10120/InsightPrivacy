#main.py
# -*- coding: utf-8 -*-
import numpy as np
from data_processing import data_processing as data_processing
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image


#output
def DrawPic(draw, font,output_list):

    Array_Row_Number = len(output_list)
    Array_Column_Number = len(output_list[0])

    InsightPrivacy = "InsightPrivacy "
    draw.text((350, 50), InsightPrivacy, font=font, align="center", fill=(41,36,33), size=1000)
    
    x = 10
    y = 120
    for index_r in range(Array_Row_Number):
        for index_c in range(Array_Column_Number):
            draw.multiline_text((x, y), col[index_c], fill=(128,128,105), font=font,align='center')
            x += 160
        x = 10
        y += 100
        return


''' contact_data = '聯絡資訊: '
    live_space = " 住址 " 
    work_space = " 工作地址 "
    mobile_number = " 行動電話\n號碼 "
    phone_number = " 住家電話號碼 "
    draw.multiline_text((10, 120), contact_data, fill=(41,36,33), font=font,align='left')
    draw.multiline_text((110, 120), live_space, fill=(128,128,105), font=font)
    draw.multiline_text((250, 120), work_space, fill=(128,128,105), font=font)
    draw.multiline_text((410, 120), mobile_number, fill=(128,128,105), font=font,align='center')
    draw.multiline_text((550, 120), phone_number, fill=(128,128,105), font=font) 

    
    financial_data = '財務資訊: '
    financial_num = " 金融機構帳戶\n  之號碼與姓名 " 
    credit_num = " 信用卡或簽帳卡\n之號碼 "
    policy_num = " 保險單號碼 "
    personal_num = " 個人之其他\n  號碼或帳戶 "
    
    draw.multiline_text((10, 220), financial_data, fill=(41,36,33), font=font,align='left')
    draw.multiline_text((100, 220), financial_num, fill=(128,128,105), font=font,align='center')
    draw.multiline_text((250, 220), credit_num, fill=(128,128,105), font=font,align='center')
    draw.multiline_text((410, 220), policy_num, fill=(128,128,105), font=font)
    draw.multiline_text((550, 220), personal_num, fill=(128,128,105), font=font,align='center')
    
    return'''







def CreatePic():

    #創建背景
    img = np.zeros((450, 450, 3), np.uint8) #黑背景
    cv2img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #如果是cv2讀取圖片才需
    cv2img[:] = (255,255,240) # 上色
    cv2img = cv2.resize(cv2img, (900, 500))
    
    # 將numpy陣列轉換為PIL影像
    imgPil = Image.fromarray(cv2img)
    
    #在圖片上加入文字
    draw = ImageDraw.Draw(imgPil)
    font = ImageFont.truetype('simhei.ttf', 20, encoding='utf-8')
    DrawPic(draw, font)

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
