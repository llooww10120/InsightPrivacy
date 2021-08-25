#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image


def listToResult(cra, module):
    list = []
    for line in range(len(module)):
        if module[line] == '1':
            temp = cra[line]
            list.append(final)
    return list



def DrawPic(draw, font, output):
    #this function will be used until the output of label will be done.

    InsightPrivacy = "InsightPrivacy"
    position_x = 10
    position_y = 120
    Tfont = ImageFont.truetype(r"FinalOutputInApp\SimHei.ttf", 40, encoding='utf-8')

    draw.text((500, 50), InsightPrivacy, font=Tfont, align="center", fill="BLUE", size=10000)
    for index in range(len(output)):
        draw.text((position_x, position_y), output[index], font=font, align="left", spacing=5)
        position_y += 20
    return


def AddTransparency(top, bottom):

    overlapping = cv2.addWeighted(bottom, 0.1, top, 0.6, 0)

    return overlapping


def CreatePic(output):

    img = cv2.imread(r"FinalOutputInApp\background.jpg")
    bottomimg = cv2.imread(r"FinalOutputInApp\background.jpg")
    img = AddTransparency(img, bottomimg)

    img = cv2.resize(img, (2000, 1000))

    imgPillow = Image.fromarray(img)

    draw = ImageDraw.Draw(imgPillow)

    font = ImageFont.truetype(r"FinalOutputInApp\SimHei.ttf", 20, encoding='utf-8')

    DrawPic(draw, font, output)

    img = np.array(imgPillow)

    # cv2.imshow('Final', img)

    # cv2.waitKey(100000)

    cv2.imwrite('result.jpg', img)
    
    return

def getListToCreatePic(cra, module):

    output = listToResult(cra, module)

    CreatePic(output)
    return
