import cv2
import numpy as np
import pytesseract


def ocr_core(image):
    test= pytesseract.image_to_string(image)
    return test



img = cv2.imread('index.png')


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#template matching
#def match_template(image, template):
#   return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 

img = get_grayscale(img)
img = remove_noise(img)
img = thresholding (img)
#img = dilate(img)
#img = erode(img)
img = opening(img)
#img = canny(img)



print(ocr_core(img))
