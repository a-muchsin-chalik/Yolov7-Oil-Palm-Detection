# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 15:50:25 2023

@author: Muchsin
"""

import numpy as np
import cv2 as cv
import os
from sklearn.preprocessing import MinMaxScaler

REGION = '3'

rgn = cv.imread('../../DATA/FOTO_UDARA/REGION_'+REGION+'/GENERATE_RESULTS/rgn.bmp', cv.IMREAD_UNCHANGED);
[r, c, band] = rgn.shape
rbn = cv.imread('../../DATA/FOTO_UDARA/REGION_'+REGION+'/GENERATE_RESULTS/rbn.bmp', cv.IMREAD_UNCHANGED);
[r, c, band] = rbn.shape
gbn = cv.imread('../../DATA/FOTO_UDARA/REGION_'+REGION+'/GENERATE_RESULTS/gbn.bmp', cv.IMREAD_UNCHANGED);
[r, c, band] = gbn.shape

for y in range(0, r-416, 316):
    for x in range(0, c-416, 316):
        print(str(y)+" "+str(x))
        y1= y   
        x1= x
        y2= y+416
        x2= x+416
        rgnROI = rgn[y1:y2, x1:x2]
        rbnROI = rbn[y1:y2, x1:x2]
        gbnROI = gbn[y1:y2, x1:x2]
        cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/IMG_GRID_RGN/"+str(y)+"_"+str(x)+".bmp", rgnROI)
        cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/IMG_GRID_RBN/"+str(y)+"_"+str(x)+".bmp", rbnROI)
        cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/IMG_GRID_GBN/"+str(y)+"_"+str(x)+".bmp", gbnROI)