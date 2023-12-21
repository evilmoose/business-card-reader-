import numpy as np 
import pandas as pd 
import cv2
import PIL
import pytesseract

img_cv = cv2.imread('./Selected/052.jpeg')

cv2.imshow('Business Card', img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()