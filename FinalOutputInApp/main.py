#!/user/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
from cv2 import cv2
from PIL import ImageFont, ImageDraw, Image

def listToResult(cra, module):
    list = []
    for line in range(len(module)):
        if module[line] == 1:
            temp = cra[line] 
            list.append(temp)
    return list


def DrawPic(draw, font, output):

    position_x = 200
    position_y = 250
    for index in range(len(output)):  # for each string in list
        if output[index] == '\n':   # if the string is new line
            continue
        list = []    # it's new list for cut string
        draw.ellipse((position_x-40, position_y+10, position_x-10, position_y+40), fill=(192, 192, 192), outline=(192, 192, 192))
        if len(output[index]) > 30:    # if the len of string is out of 30, then cut it
            length = 30
            a, width = 0, 0
            status = False
            i = 0
            while i <= math.ceil(len(output[index])/30):    # for each cut string, each length of the cut string is at most 30
                if output[index][a:length] == '\n':
                    break

                for j in range(a, length):
                    if output[index][j] == '：' or output[index][j] == '；':
                        length = j+1
                        i = i-1
                        status = True
                        width = length - a
                        break
                list.append(output[index][a:length])    #just append the cut string into the new list, then move the index just as the same way with lseek
                if length == len(output[index]):
                    break
                i+=1
                if status:
                    a += width
                    status = False
                else:
                    a += 30
                if length + 30 <= len(output[index]):   #verify the next position of the index
                    length += 30
                else:
                    length = len(output[index])

        else:
            list.append(output[index])
        for i in list:
            if index % 2 == 0:
                draw.text((position_x, position_y), i, font=font, align="left", spacing=5)
            else:
                draw.text((position_x, position_y), i, font=font, align="left", spacing=5, fill=(255, 255, 0))
            position_y += 70
        draw.line([(position_x, position_y), (position_x + 1200, position_y)], fill=(192, 192, 192), width=5)
        position_y += 20

    return


def AddTransparency(top, bottom):

    overlapping = cv2.addWeighted(bottom, 1, top, 0, 0)

    return overlapping


def CreatePic(output):

    img = cv2.imread('background.jpg')
    bottomimg = cv2.imread('background.jpg')
    img = AddTransparency(img, bottomimg)

    img = cv2.resize(img, (1633, 2903))

    #cv2.line(img, (0, 0), (2500, 0), (0, 0, 0), 40)
    #cv2.line(img, (0, 0), (0, 1500), (0, 0, 0), 40)
    #cv2.line(img, (2500, 0), (2500, 1500), (0, 0, 0), 40)
    #cv2.line(img, (0, 1500), (2500, 1500), (0, 0, 0), 40)

    imgPillow = Image.fromarray(img)

    draw = ImageDraw.Draw(imgPillow)

    font = ImageFont.truetype('Font.ttf', 40, encoding='utf-8')

    DrawPic(draw, font, output)

    img = np.array(imgPillow)

    cv2.imshow('Final', img)

    cv2.waitKey(100000)

    cv2.imwrite('result.jpg', img)



def getListToCreatePic(cra, module):

    output = listToResult(cra, module)

    CreatePic(output)
    return
