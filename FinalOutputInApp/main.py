import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image

img = ((450, 450, 3), np.uint8)

#img[:] = (0, 0, 255)

gain_data = '索取資料:'
gain_text = "個人檔案資料n" + "發佈的文字、圖片、影片\n" + "其他用戶發佈關於您的照片\n"

using_way = "用途:"
using_text = "提供及維護服務\n" + "開發及改善服務\n" + "安全性及防止未經授權的使\n" + "用為您提供優化內容\n"

precaution = "注意事項:"
precaution_text = "刪除帳號後，企業會保存你的資料一段時間，而契約中無法得知一段時間是指多久\n"

font_path = "./康熙字典體.ttf"

font = ImageFont.truetype(font_path, 192, encoding="utf-8")

imgPillow = Image.fromarray(img)

draw = ImageDraw.Draw(imgPillow)
draw.text((10, 120), gain_data, font=font, align="left")
draw.text((10, 140), gain_text, font=font, spacing=2)
draw.text((10, 220), using_way, font=font, align="left")
draw.text((10, 240), using_text, font=font, spacing=2)
draw.text((10, 320), precaution, font=font, align="left")
draw.text((10, 340), precaution_text, font=font, spacing=2)

img = np.array(imgPillow)
cv2.imshow("Final", img)
cv2.waitKey(10)
cv2.destroyWindow()
