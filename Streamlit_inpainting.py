import cv2
from PIL import Image
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import time

# global erase
# erase= False
# img = cv2.imread(r'C:\Users\PoojaT\Desktop\soccor_ball.jpg')
# image= img.copy()

# def mask_obj(event, x, y, flags, param):
#     global erase
#     if event == cv2.EVENT_LBUTTONDOWN:
#         erase= True
#         cv2.circle(image, (x, y), 10, (255,255,0, 0.3), -1)
    
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if erase == True:
#             cv2.circle(image, (x, y), 10, (255,255,0, 0.3), -1)

#     elif event == cv2.EVENT_LBUTTONUP:
#         erase = False         

# cv2.namedWindow('Input')
# cv2.setMouseCallback('Input', mask_obj)

# while(1):
#     cv2.imshow('Input',image)
#     cv2.imwrite('mask.png',image)
#     if cv2.waitKey(20) & 0xFF == 27:
#         break
    
# img2= cv2.imread('mask.png')
# diff= cv2.bitwise_xor(img2, img)
# diff= cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

# for i in range(diff.shape[0]):
#     for j in range(diff.shape[1]):
#         if diff[i][j]!= 0:
#             diff[i][j]= 255

# # masked= cv2.bitwise_xor(img, img, mask=diff)
# # cv2.imshow('output', masked)

# masked1= cv2.bitwise_and(img, img, mask=diff)
# cv2.imshow('Masked image', masked1)

# # diff = diff[:,:,0]
# # print(diff.shape)
# cv2.imshow('Binary mask', diff)
# # cv2.imshow('mask1', diff[:,:, 0])
# # cv2.imshow('mask2', diff[:,:, 1])
# # cv2.imshow('mask3', diff[:,:, 2])

# dst = cv2.inpaint(img, diff, 1,cv2.INPAINT_TELEA)
# cv2.imshow('Fast Marching Method based Inpainting', dst)

# dst1 = cv2.inpaint(img, diff, 3, cv2.INPAINT_NS)
# cv2.imshow('Navier-Stokes based Inpainting', dst1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

##############################Streamlit####################################################################
# background setting
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSA1i7-Ezu7CAToF8XdsqHAgPSFc6ulGuGqTA&usqp=CAU");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown("<h1> OpenCV: Image Inpainting </h1>",  unsafe_allow_html=True)

stroke_width= st.sidebar.slider("Choose stroke width", 0, 100, 30)
color = st.sidebar.color_picker('Pick stroke Color', )

#upload image
upload=st.file_uploader("Upload image", ['png', 'jpg'])
if upload is not None:
    # streamlit canvas to draw mask
    img= Image.open(upload)
    canvas= st_canvas(
        background_image= img,
        stroke_width= stroke_width,
        stroke_color=color,
        width = img.size[0],
        height= img.size[1],
        drawing_mode= "freedraw"

    )
    if st.button('Process Image'):

        diff= cv2.cvtColor(canvas.image_data, cv2.COLOR_BGR2GRAY)
        for i in range(diff.shape[0]):
            for j in range(diff.shape[1]):
                if diff[i][j]!= 0:
                    diff[i][j]= 255
        c1, c2= st.columns(2)
        c1.subheader(" Binary Mask")
        c1.image(diff)

        img= np.asarray(img)
        masked1= cv2.bitwise_and(img, img, mask=diff)
        c2.subheader("Masked image 1")
        c2.image(masked1)

        # masked2= cv2.bitwise_not(cv2.bitwise_xor(img, img, mask= diff))
        # c3.subheader("Masked image 2")
        # c3.image(masked2)
        
        # Fast Marching Method
        c3, c4= st.columns(2)
        t1= time.time()
        dst = cv2.inpaint(img, diff, 1,cv2.INPAINT_TELEA)
        t2= time.time()
        c3.subheader("Fast Marching Method based Inpainting")
        c3.image(dst)
        c3.write('Computational time')
        c3.write(t2-t1)

        #Navier-Stokes
        t3= time.time()
        dst1 = cv2.inpaint(img, diff, 1, cv2.INPAINT_NS)
        t4= time.time()
        c4.subheader("Navier-Stokes based Inpainting")
        c4.image(dst1)
        c4.write('Computational time')
        c4.write(t4-t3)