import numpy as np 
import pandas as pd 
import cv2
import PIL
import pytesseract

img_cv = cv2.imread('./Selected/052.jpeg')
print(img_cv)

cv2.imshow('Business Card', img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_pl = PIL.Image.open('./Selected/052.jpeg')
print(img_pl)

# Extract Text from Image using 'cv2'
text_cv = pytesseract.image_to_string(img_cv)
print(text_cv)

# Extract Text from Image using 'PIL'
text_pl = pytesseract.image_to_string(img_pl)
print(text_pl)

# Image to data using PyTesseract
data = pytesseract.image_to_data(img_cv)
print(data)

# Spit data by new line('\n')
print(data.split('\n'))
print(list(map(lambda x: x.split('\t'), ['level\tpage_num\tblock_num\tpar_num\tline_num\tword_num\tleft\ttop\twidth\theight\tconf\ttext'])))
dataList = list(map(lambda x: x.split('\t'), data.split('\n')))
print(dataList)

# get all the list of colunms
df = pd.DataFrame(dataList[1:], columns=dataList[0])
print(df)
print(df.head(10))
print(df.info())

# data prederation

# drop missing values and rows
df.dropna(inplace=True)

# change the dataType
col_int = ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf']

df[col_int] = df[col_int].astype(float).astype(int)


print(df.dtypes)

# Drawing Bounding Box around each word
image = img_cv.copy()
level = 'page'

for l, x, y, w, h, c in df[['level', 'left', 'top', 'width', 'height', 'conf']].values:
    
    if level == 'page':
        if l == 1:  # page is equal to 1
            # Draw the bounding box
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0,), 2) 
            # cv2.rectangle(
                # Image,
                # Point 1,
                # Point 2 (diagnol),
                # Color,
                # Line Weight) 
        else:
            continue
    elif level == 'block':
        if l == 2:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0,), 2)
        else:
            continue
    elif level == 'para':
        if l == 3:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0,), 2)
        else:
            continue
    elif level == 'word':
        if l == 4:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255,), 2)
        else:
            continue
    elif level == 'line':
        if l == 5:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0,), 2)
        else:
            continue

# Draw the box
cv2.imshow("bounding box", image)
cv2.waitKey()
cv2.destroyAllWindows()