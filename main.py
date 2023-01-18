# TechVidvan Object detection of similar color

import cv2
import numpy as np
import time 

from depthai_sdk import OakCamera
import depthai as dai

# Create pipeline
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
        

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    # find the colors within the boundaries

    # lower bound and upper bound for cyan

    lower_bound_c = np.array([100,100,90])
    upper_bound_c = np.array([255,255,130])

    # lower and upper bound for magenta

    lower_bound_m = np.array([100, 20, 100])
    upper_bound_m = np.array([255,80,255])

    # lower and upper bound for yellow

    lower_bound_y = np.array([70, 130, 130])
    upper_bound_y = np.array([120, 255, 255])


    mask = cv2.inRange(frame, lower_bound_y, upper_bound_y)


    # define kernel size  
    kernel = np.ones((7,7),np.uint8)

    # Remove unnecessary noise from mask

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Segment only the detected f
    segmented_img = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours from the mask

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = cv2.drawContours(segmented_img, contours, -1, (0, 255, 0), 3)

    # Draw contour on original image

    output = cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    amount_c = contours

    # Showing the output

    cv2.imshow("cam", output)
    cv2.imshow("mask", mask)
    if (cv2.waitKey(30) == 27):
       break
