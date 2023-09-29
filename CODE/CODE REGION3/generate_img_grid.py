# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:50:25 2023

@author: Muchsin
"""

import numpy as np
import cv2 as cv
from sklearn.preprocessing import MinMaxScaler

REGION = '3'

img = cv.imread('../DATA/FOTO_UDARA/REGION_'+REGION+'/GENERATE_RESULTS/rgb.bmp', cv.IMREAD_UNCHANGED);
[r, c, band] = img.shape

for y in range(0, r-416, 316):
    for x in range(0, c-416, 316):
        print(str(y)+" "+str(x))
        y1= y   
        x1= x
        y2= y+416
        x2= x+416
        rgbROI = img[y1:y2, x1:x2]
        cv.imwrite("../DATA/FOTO_UDARA/REGION_"+REGION+"/IMG_GRID/"+str(y)+"_"+str(x)+".bmp", rgbROI)