import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.ones(input_image.shape, dtype=np.uint8)*255
     

    input_hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    output = cv2.inRange(input_hsv, (0, 15, 15), (200, 255,255))
    
    # Write your code here for output
    
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
