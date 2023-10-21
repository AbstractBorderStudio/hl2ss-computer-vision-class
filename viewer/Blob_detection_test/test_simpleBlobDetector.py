#Non funziona con i pallini bianchi su sfondo nero -> bisogna invertire l'immagine, aumentare il contrasto
#Non capisco come funzionano i parametri

import numpy as np
import cv2 
import sys

np.set_printoptions(threshold=sys.maxsize)

# Read image
path = f"../output/imgs/depth/frame8.png" 
im = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200
 
# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.2
 
# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.3
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01
 
# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
  detector = cv2.SimpleBlobDetector(params)
else : 
  detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im)

print(keypoints)
# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
 
# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)