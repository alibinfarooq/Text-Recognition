import cv2
import pytesseract
import matplotlib.pyplot as plt

img=cv2.imread('index.png')

image2char=pytesseract.image_to_string(img)

print(image2char)

imgbox = pytesseract.image_to_boxes(img)

type(imgbox)

print(imgbox)

imgH,imgW,_ = img.shape

for boxes in imgbox.splitlines():
    boxes = boxes.split(' ')
    x,y,w,h = int(boxes[1]),int(boxes[2]),int(boxes[3]),int(boxes[4])
    cv2.rectangle(img, (x, imgH-y),(w,imgH-h),(0,0,255),3)



plt.imshow(cv2,cvtColor(img, cv2,COLOR_BGR2RGB))