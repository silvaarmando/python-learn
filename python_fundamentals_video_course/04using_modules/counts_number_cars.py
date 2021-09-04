import cv2
import matplotlib.pyplot as plt
import cvlib as cv 
from cvlib.object_detection import draw_bbox

img = cv2.imread('cars_image.jpgeg')
bbox, label, conf = cvimagedetect_common_objects(img)
output_image = draw_bbox(img, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print(f'Number of cars in the image is' + str(label.count('car')))
