#main.py
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image

#output
def DrawPic(draw, font, output_list):
    
    Array_Row_Number = len(output_list)

    InsightPrivacy = "InsightPrivacy "
    draw.text((350, 50), InsightPrivacy, font=font, align="center", fill=(41,36,33), size=1000)
    
    x = 10
    y = 120
    for index_r in range(0,Array_Row_Number):
        Array_Column_Number = len(output_list[Array_Row_Number])
        for index_c in range(0,Array_Column_Number):
            draw.multiline_text((x, y), output_list[Array_Row_Number][Array_Column_Number], fill=(128,128,105), font=font,align='center')
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
    
    return
'''






def CreatePic():

    output_list = [
        ['聯絡資訊', '住址', '工作地址', '以前地址', '住家電話號碼', '行動電話', '即時通帳號', '網路平臺申請之帳號', '通訊及戶籍地址',
            '相片', '指紋', '電子郵遞地址', '電子簽章', '憑證卡序號', '憑證序號', '提供網路身分認證或申辦查詢服務之紀錄', '電子信箱'],
        ['財務資訊', '金融機構帳戶之號碼與姓名', '信用卡或簽帳卡之號碼', '保險單號碼', '個人之其他號碼或帳戶'],
        ['姓名', '生日', '名字'],
        ['身分證號', '統一編號', '身分證統一編號', '統一證號', '稅籍編號', '保險憑證號碼',
            '殘障手冊號碼', '退休證之號碼', '證照號碼', '護照號碼', '身分證字號'],
        ['瀏覽資訊 IP 位址', '設備資訊', '藍芽聯絡人', '郵遞區號', '手機製造商', '手機型號', 'UDID']
    ]
    
    #創建背景
    img = np.zeros((450, 450, 3), np.uint8) #黑背景
    cv2img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #如果是cv2讀取圖片才需
    cv2img[:] = (255,255,240) # 上色
    cv2img = cv2.resize(cv2img, (900, 500))
    
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
