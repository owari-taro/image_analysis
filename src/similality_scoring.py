
import cv2
import os
IMG_SIZE = (200, 200)

def create_hist(image_fname: str):
    img = cv2.imread(image_fname)
    img = cv2.resize(img, IMG_SIZE)
    img_hist = cv2.calcHist([target_img], [0], None, [256], [0, 256])
    return img_hist


files = os.listdir(IMG_sDIR)
for file in files:
    if file == '.DS_Store' or file == TARGET_FILE:
        continue

    comparing_img_path = IMG_DIR + file
    comparing_img = cv2.imread(comparing_img_path)
    comparing_img = cv2.resize(comparing_img, IMG_SIZE)
    comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0, 256])

    ret = cv2.compareHist(target_hist, comparing_hist, 0)
    print(file, ret)
