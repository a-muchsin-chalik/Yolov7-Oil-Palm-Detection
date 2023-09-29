# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 14:08:39 2023

@author: Muchsin
"""
#import library
import cv2 as cv
from sklearn.preprocessing import MinMaxScaler
import os

REGION = '2'

#read image
img = cv.imread ('../../DATA/FOTO_UDARA/REGION_'+REGION+'/FOTO_UDARA_2.tif', cv.IMREAD_UNCHANGED)

#rotate image
height, width = img.shape[:2]
R = cv.getRotationMatrix2D((width/2, height/2), 31.4, 1)
rotation = cv.warpAffine(img, R, (width, height))

#Cropped Image
w=2943
h=3561
t=80
b=80
l=777
r=787
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
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgb.jpg", img_rgb)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgb.tif", img_rgb)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgb.bmp", img_rgb)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rgn.bmp", img_rgn)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/rbn.bmp", img_rbn)
cv.imwrite("../../DATA/FOTO_UDARA/REGION_"+REGION+"/GENERATE_RESULTS/gbn.bmp", img_gbn)