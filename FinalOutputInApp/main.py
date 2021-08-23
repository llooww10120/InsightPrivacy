#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image


def openfile(file1, file2):
    with open(file1, 'r', encoding='utf8') as f1:
        input = f1.readlines()
    with open(file2, 'r', encoding='utf8') as f2:
        module = f2.readlines()
    list = []
    for line in range(len(module)):
        if module[line] == '1\n':
            temp = input[line]
            final = temp.split('，')
            for i in range(len(final)):
                list.append(final[i])
    return list



def DrawPic(draw, font, output):
    #this function will be used until the output of label will be done.

    InsightPrivacy = "InsightPrivacy "
    position_x = 10
    position_y = 120
    draw.text((500, 50), InsightPrivacy, font=font, align="center", fill="BLUE", size=10000)
    for index in range(len(output)):
        draw.text((position_x, position_y), output[index], font=font, align="left", spacing=5)
        position_y += 40
    return


def AddTransparency(top, bottom):

    overlapping = cv2.addWeighted(bottom, 0.1, top, 0.2, 0)

    return overlapping


def CreatePic(output):

    img = cv2.imread('background.jpg')
    bottomimg = cv2.imread('background.jpg')
    img = AddTransparency(img, bottomimg)

    img = cv2.resize(img, (1500, 1000))

    imgPillow = Image.fromarray(img)

    draw = ImageDraw.Draw(imgPillow)

    font = ImageFont.truetype('simhei.ttf', 30, encoding='utf-8')

    DrawPic(draw, font, output)

    img = np.array(imgPillow)

    cv2.imshow('Final', img)

    cv2.waitKey(100000)

    cv2.imwrite('result.jpg', img)

if __name__== "__main__":
    output = openfile('input.txt', 'module_output.txt')
    CreatePic(output)
