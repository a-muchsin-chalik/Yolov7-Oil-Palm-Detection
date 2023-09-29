# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:08:39 2023

@author: Muchsin
"""
#import library
import cv2 as cv
from sklearn.preprocessing import MinMaxScaler
import os

REGION = '3'

#read image
img = cv.imread ('../../DATA/FOTO_UDARA/REGION_'+REGION+'/FOTO_UDARA_3.tif', cv.IMREAD_UNCHANGED)

#rotate image
height, width = img.shape[:2]
R = cv.getRotationMatrix2D((width/2, height/2), 3.37, 1)
rotation = cv.warpAffine(img, R, (width, height))

#Cropped Image
w=3458
h=1502
t=95
b=65
l=15
r=10
cropped = rotation[t:h-b, l:w-r]

#processing layer division
scaler = MinMaxScaler(feature_range=(0, 255))
img_b = cropped[:,:,0]
img_g = cropped[:,:,1]
img_r = cropped[:,:,2]
img_n = cropped[:,:,3]
img_rgb = cv.merge((img_b,img_g,img_r))
img_rgn = cv.merge((img_r,img_g,img_n))
img_rbn = cv.merge((img_r,img_b,img_n))
img_gbn = cv.merge((img_g,img_b,img_n))

#Result image
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/blue.bmp", img_b)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/green.bmp", img_g)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/red.bmp", img_r)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/nir.bmp", img_n)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgb.bmp", img_rgb)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgn.bmp", img_rgn)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rbn.bmp", img_rbn)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/gbn.bmp", img_gbn)