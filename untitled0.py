# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:37:55 2024

@author: goldenbullhornPC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Yellow box.
yellow = cv2.imread('input/yellow.jpg')

# Step 1. Transfer color to HSV
hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
hsv_yellow_h = hsv_yellow[:,:,0]
hsv_yellow_s = hsv_yellow[:,:,1]
hsv_yellow_v = hsv_yellow[:,:,2]

# Step 2. Setting the color range and filter the image.
lower_yellow = np.array([170, 0, 0])
upper_yellow = np.array([180, 255, 255])
mask = cv2.inRange(hsv_yellow, lower_yellow, upper_yellow)

print("Type of mask:", type(mask))
print("Size of mask:", mask.size)
print("Data type of mask elements:", mask.dtype)

kernel = np.ones((10, 10), np.uint8)
dilated_mask = cv2.dilate(mask, kernel, iterations=1)

# Step 3. Binary the image, find the left-top and right-bottom coordinate (x, y, w, h) or (x1, x2, y1, y2).
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(cv2.cvtColor(hsv_yellow, cv2.COLOR_HSV2BGR))
axes[1].imshow(dilated_mask)

# Step 4. Crop the image by the coordinate.
crop_edge = 20  # surrounding 20 pixels 
cropHSV_yellow = yellow[y-crop_edge: y+h+crop_edge, x-crop_edge: x+w+crop_edge]   # take (x, y, w, h) as example.
