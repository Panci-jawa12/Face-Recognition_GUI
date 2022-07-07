import cv2

x_start, y_start, x_end, y_end = 0, 0, 0, 0
Jendela = "Original Image"

def crop_image(event,x,y,flags,param):
    
    global x_start, y_start, x_end, y_end
    
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x,y,x,y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        x_end, y_end = x, y
        
    elif event == cv2.EVENT_LBUTTONUP:
        cropped_img = image[y_start:y_end, x_start:x_end]
        cv2.imshow("Cropped Image", cropped_img)
        cv2.imwrite("naise.png", cropped_img)
        print("gambar kesave dong")
        
    # elif event == cv2.EVENT_RBUTTONDOWN:
    #     cropped_img = image[y_start:y_end, x_start:x_end]
    #     cv2.imwrite("naise.jpg", cropped_img)
    #     print("gambar kesave dong")
        
cv2.namedWindow(Jendela)
cv2.setMouseCallback(Jendela, crop_image)

image = cv2.imread(filename='image/signup.png')

while True:
    cv2.imshow(Jendela, image)
    if cv2.waitKey(1) == ord('q'):
        break
        
cv2.destroyAllWindows()