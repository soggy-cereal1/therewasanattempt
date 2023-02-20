import cv2
import numpy

cap = cv2.VideoCapture(2)
img = cap.read()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply thresholding to convert grayscale to binary image
ret,thresh = cv2.threshold(gray,150,255,0)

# find the contours
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Number of objects detected:", len(contours))

# define function to compute aspect ratio
def aspect_ratio(cnt):
   x, y, w, h = cv2.boundingRect(cnt)
   ratio = float(w)/h
   return ratio

# select first contour
cnt = contours[0]

# find the aspect ratio
ar = aspect_ratio(cnt)

# round it to two decimal points
ar = round(ar, 2)

# draw contours
cv2.drawContours(img,[cnt],0,(0,255,0),2)

# draw bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# put text on the image
cv2.putText(img, f'Aspect Ratio={ar}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
print(f"Aspect Ratio of object 1 =", ar)
cv2.imshow("Aspect Ratio", img)
cv2.waitKey(0)
cv2.destroyAllWindows()