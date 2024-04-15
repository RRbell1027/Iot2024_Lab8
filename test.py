import cv2
import numpy as np
image = cv2.imread("TW.jpg")    #先讀取圖片

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray_by_hand = cv2.imread('TW.jpg')

# Extract RGB channels
red_channel = gray_by_hand[:, :, 2]
green_channel = gray_by_hand[:, :, 1]
blue_channel = gray_by_hand[:, :, 0]

# Convert to grayscale manually
gray_by_hand = 0.2989 * red_channel + 0.5870 * green_channel + 0.1140 * blue_channel
gray_by_hand = gray_by_hand.astype(np.uint8)

ret, binary_image = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

cv2.imshow("Sun", image) # origin
cv2.imshow("gray", gray) # gray scale by opencv library function
cv2.imshow("gbh", gray_by_hand) # gray scale by custom code above
cv2.imshow("bimg", binary_image) # binarize by opencv library function

cv2.waitKey(0)            #等待 enter被按下
cv2.destroyAllWindows()