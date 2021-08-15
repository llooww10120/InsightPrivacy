#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image


def DrawPic(draw, font):
    #this function will be used until the output of label will be done.

    InsightPrivacy = "InsightPrivacy "

    gain_data = '索取資料:\n'
    gain_text = "個人檔案資料\n" + "發佈的文字、圖片、影片\n" + "其他用戶發佈關於您的照片\n"

    using_way = "用途:\n"
    using_text = "提供及維護服務\n" + "開發及改善服務\n" + "安全性及防止未經授權的使用\n" + "為您提供優化內容\n"

    precaution = "注意事項:\n"
    precaution_text = "刪除帳號後，企業會保存你的資料一段時間，而契約中無法得知一段時間是指多久\n"

    draw.text((350, 50), InsightPrivacy, font=font, align="center", fill="BLUE", size=1000)
    draw.text((10, 120), gain_data, font=font, align="left", spacing=5)
    draw.text((10, 140), gain_text, font=font, spacing=2)
    draw.text((10, 220), using_way, font=font, align="left", spacing=5)
    draw.text((10, 240), using_text, font=font, spacing=2)
    draw.text((10, 320), precaution, font=font, align="left", spacing=5)
    draw.text((10, 340), precaution_text, font=font, spacing=2)
    return


def AddTransparency(top, bottom):

    overlapping = cv2.addWeighted(bottom, 0.1, top, 0.2, 0)

    return overlapping


def CreatePic():

    img = cv2.imread('background.jpg')
    bottomimg = cv2.imread('background.jpg')
    img = AddTransparency(img, bottomimg)

    img = cv2.resize(img, (900, 500))

    imgPillow = Image.fromarray(img)

    draw = ImageDraw.Draw(imgPillow)

    font = ImageFont.truetype('simhei.ttf', 20, encoding='utf-8')

    DrawPic(draw, font)

    img = np.array(imgPillow)

    cv2.imshow('Final', img)

    cv2.waitKey(100000)

    cv2.imwrite('result.jpg', img)

if __name__== "__main__":
    CreatePic()
