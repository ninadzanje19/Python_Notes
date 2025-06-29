from PIL import Image
import cv2

#open an image
"""im = Image.open("data\page_01.jpg")"""

#display an image
"""print(im.show())"""

#The image is stored as an object
"""print(im)"""

#Rotates the image by given degrees
"""im_rotated = im.rotate(90)"""

#saves the image at the given address wit hthe given name
"""im_rotated.save("data\page_01_rotated.jpg")"""


#read the image using open CV
image = cv2.imread("data\page_01.jpg")

#Displaying the image
"""cv2.imshow("Title", image)"""
#Time for which the image should be displayed in ms, 0 for Infinity
"""cv2.waitKey(0)"""

#Invert an Image's colours
inverted_image = cv2.bitwise_not(image)
#display an Image(title, img obj)
"""cv2.imshow("Inverted Image", inverted_image)"""
#Write an Image(address, img obj)
"""cv2.imwrite("data\Inverted_Image.jpg", inverted_image)"""

#Greyscale an image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Binarizing an image, Grayscaling improves img for binarization
thresh, im_bw = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("Biniarized Image", im_bw)
cv2.waitKey(0)