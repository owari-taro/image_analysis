
import cv2
import os
IMG_SIZE = (200, 200)


def create_hist(image_fname: str):
    img = cv2.imread(image_fname)
    img = cv2.resize(img, IMG_SIZE)
    img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return img_hist


def compare(img1: str, img2: str):
    hist1, hist2 = create_hist(img1), create_hist(img2)
    score = cv2.compareHist(hist1, hist2, 0)
    print(score)
    return score


if __name__ == "__main__":
    img1 = "img1_1.png"
    img11 = "img1_2.png"
    img2 = "img2_1.png"
    compare(img1, img11)
    compare(img1, img2)
