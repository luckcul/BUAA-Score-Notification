#coding=utf-8

from PIL import Image
# from PIL import ImageEnhance
# from PIL import ImageFilter
import sys
from pytesser import *

# 二值化
def set_table(threshold) :
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else :
            table.append(1)
    return table 

def  ocr(name, threshold = 150):
    
    #打开图片
    im = Image.open(name)
    #转化到亮度
    imgry = im.convert('L')
    imgry.save('g'+name)
    #二值化
    out = imgry.point(set_table(threshold),'1') #在pytesser 目录里 要变更路径
    # 观察全部threshold在[0,255]的情况，选择最优的threshold
    # for i in range(255):
    #     out = imgry.point(set_table(i), '1')
    #     out.save(str(i) + name)
    # #识别
    import os
    os.chdir(r'C:\Users\luckcul\Anaconda2\Lib\site-packages\pytesser_v0.0.1')

    text = image_to_string(out)
    os.chdir(r'E:\code\pushScore')
    text = text.strip()
    text = ''.join(text.split())
    text = text.upper();
    return text

if __name__ == '__main__':
    print ocr("image.jpg", 125)