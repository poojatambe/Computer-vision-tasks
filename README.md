# Opencv_computer_vision

**Image Inpainting**

Image inpainting is a computer vision algorithm used to fill regions inside an image or video. The region to be filled is identified by a binary mask and neighboring pixels are used to fill the region.

The OpenCV provides image inpainting functionality with cv2.inpaint. It supports 2 algorithms.
1. Fast Marching Method
2. Navier-Stokes

Results:
![soccor_ball](https://user-images.githubusercontent.com/64680838/205074004-94609c00-2043-48eb-973c-c54ce2b01203.jpg)
![image](https://user-images.githubusercontent.com/64680838/205074167-dbceac8d-517d-4cd1-a0c5-8f89a03b1acd.png)


**Template Matching**

This method is used to find a template image’s location in a larger image. The matching is performed by sliding the template over the input image as 2D convolution. The template and patch of the input image under the template are compared. 

The OpenCV provides the function cv2.matchTemplate: Cv2.matchTemplate(image, template, method, result, mask)		

Results:
1. Multiple occurance of template:

![image](https://user-images.githubusercontent.com/64680838/205848285-c47a2bf2-cfb2-42e3-8b9b-aaf8e6e3fc42.png)
2.Single occurance of template:

![image](https://user-images.githubusercontent.com/64680838/205848332-60f537f8-6648-4934-b37f-84f62089fdab.png)
