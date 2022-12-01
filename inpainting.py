import cv2
from PIL import Image
import numpy as np
# import streamlit as st
# from streamlit_drawable_canvas import st_canvas
import time

global erase
erase= False

# Read image
img = cv2.imread('./soccor_ball.jpg')
image= img.copy()

def mask_obj(event, x, y, flags, param):
    global erase
    if event == cv2.EVENT_LBUTTONDOWN:
        erase= True
        cv2.circle(image, (x, y), 20, (255,255,0, 0.3), -1)
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if erase == True:
            cv2.circle(image, (x, y), 20, (255,255,0, 0.3), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        erase = False         

cv2.namedWindow('Input')
cv2.setMouseCallback('Input', mask_obj)

while(1):
    cv2.imshow('Input',image)
    cv2.imwrite('mask.png',image)
    if cv2.waitKey(20) & 0xFF == 27: #press esc to generate results
        break
    
img2= cv2.imread('mask.png')
diff= cv2.bitwise_xor(img2, img)
diff= cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

for i in range(diff.shape[0]):
    for j in range(diff.shape[1]):
        if diff[i][j]!= 0:
            diff[i][j]= 255

# masked= cv2.bitwise_xor(img, img, mask=diff)
# cv2.imshow('output', masked)

#masked image
masked1= cv2.bitwise_and(img, img, mask=diff)
cv2.imshow('Masked image', masked1)

# diff = diff[:,:,0]
# print(diff.shape)

# binary mask
cv2.imshow('Binary mask', diff)

# cv2.imshow('mask1', diff[:,:, 0])
# cv2.imshow('mask2', diff[:,:, 1])
# cv2.imshow('mask3', diff[:,:, 2])

# Method1:Fast Marching
dst = cv2.inpaint(img, diff, 1,cv2.INPAINT_TELEA)
cv2.imshow('Fast Marching Method based Inpainting', dst)

#Method2:Navier-Stokes
dst1 = cv2.inpaint(img, diff, 3, cv2.INPAINT_NS)
cv2.imshow('Navier-Stokes based Inpainting', dst1)

cv2.waitKey(0)
cv2.destroyAllWindows()

