import cv2

img = cv2.imread('c:/Users/ASUS/PycharmProjects/pythonProject/image/menu.png')

#resize image (new_width, new_heigth)
img_resize = cv2.resize(img, (8, 8))

#show image
# cv2.imshow('Original Image', img)
cv2.imshow('Resize Image', img_resize)
cv2.imwrite("image/menu1.png", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()