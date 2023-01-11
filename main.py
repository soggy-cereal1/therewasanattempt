# TechVidvan Object detection of similar color

import cv2
import numpy as np
# from depthai_sdk import OakCamera
# import depthai as dai

# # Create pipeline
# pipeline = dai.Pipeline()
# cam = pipeline.create(dai.node.ColorCamera)
# cam.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)
# cam.setPreviewSize(1280,720)
# xout = pipeline.create(dai.node.XLinkOut)
# xout.setStreamName("rgb")
# cam.preview.link(xout.input)

# # Connect to device and start pipeline
# with dai.Device(pipeline) as device, pyvirtualcam.Camera(width=1280, height=720, fps=20) as uvc:
#     qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
#     print("UVC running")
#     while True:
#         frame = qRgb.get().getFrame()
#         uvc.send(frame)
        
# Reading the image
img = cv2.imread("IMG_4206.jpg")

# convert to hsv colorspace

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# lower bound and upper bound for blue color
lower_bound = np.array([64, 10, 10])
upper_bound = np.array([255, 75, 75])	 

# I can't tell what i did but hte above detects the cube's lines and the below detects light colors
# I suck at visualizing things what does this mean
# HSV doesn't work, i tried BGR for ^ and RGB for below the same values but flipped

# HSV is an attempt at the below because what is going on

# lower_bound = np.array([170, 10, 100])
# upper_bound = np.array([258, 100, 100])	 


# find the colors within the boundaries
mask = cv2.inRange(img, lower_bound, upper_bound)


# define kernel size  
kernel = np.ones((7,7),np.uint8)

# Remove unnecessary noise from mask

mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Segment only the detected region
segmented_img = cv2.bitwise_and(img, img, mask=mask)

# Find contours from the mask

contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 3)

# Showing the output

# cv2.imshow("Output", output)

# lower bound and upper bound for red color

# lower_bound = np.array([5, 22, 22])
# upper_bound = np.array([340, 25, 24])	 

# Draw contour on original image

output = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)


# Showing the output

cv2.imshow("Image", img)
cv2.imshow("mask", mask)


cv2.waitKey(0)
cv2.destroyAllWindows()