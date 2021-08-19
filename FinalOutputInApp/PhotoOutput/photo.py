# -*- coding: utf-8 -*-

from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np


# cv2讀取圖片
img = cv2.imread('tmp.jfif')
cv2img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)# cv2和PIL中颜色的hex码的储存顺序不同 
pilimg = Image.fromarray(cv2img)

# 透過PIL印出漢字
draw = ImageDraw.Draw(pilimg) # 圖片上印字
font = ImageFont.truetype("simhei.ttf", 20, encoding="utf-8") # 參數1:字體文件路徑, 參數2:字體大小
        # 1.打印座標(x.y), 2.文本,    3.字體顏色,   4.字體
draw.text((0, 0), "所使用的個人隱私", (41, 36, 33), font=font) 

# PIL圖片轉 cv2 圖片
cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
# cv2.imshow("图片", cv2charimg) # 汉字窗口标题显示乱码
cv2.imshow("photo", cv2charimg)
