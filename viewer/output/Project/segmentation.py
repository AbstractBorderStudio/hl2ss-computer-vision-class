import cv2
import numpy as np
from matplotlib import pyplot as plt

def FindCirclesFine(img):
    """
    Blob detection using cv2.HoughCircles
    """

    # grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # increase contrast via equalization
    #eq = cv2.equalizeHist(gray)

    # Apply a smoothing kernel to make gaussian blur
    # this reduce noise. Improves edge detection.
    smoothed = cv2.GaussianBlur(gray, (9,9), cv2.BORDER_DEFAULT)

    # threshold
    thresh = cv2.threshold(smoothed, 80, 255, cv2.THRESH_BINARY)[1]

    # compute Canny edge detection
    edges = cv2.Canny(thresh, 75, 150, apertureSize=3)

    # apply dialtion to highlight circlular areas.
    dilation = cv2.dilate(edges, np.ones((2,2)), iterations=2)

    # apply hough transform to detect circles
    circles = cv2.HoughCircles(dilation, cv2.HOUGH_GRADIENT, dp=1, minDist=10, param1=150, param2=10, minRadius=10, maxRadius=20)
    # add circles to images
    for circle in circles[0,:]:
        x, y, r = circle
        center = (x,y)
        cv2.circle(gray, (int(x), int(y)), int(r), (255,0,0), cv2.FILLED)

    return gray#cv2.hconcat([thresh, dilation, gray])




# =========== simple blob detection param initialization ===========

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 20
params.maxThreshold = 200

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.5

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.5

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.1

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
    detector = cv2.SimpleBlobDetector(params)
else : 
    detector = cv2.SimpleBlobDetector_create(params)



def FindCirclesSimpleBlob(img):
    """
    Blob detection using cv2.SimpleBlobDetector
    """

    # grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # increase contrast via equalization
    #eq = cv2.equalizeHist(gray)

    # Apply a smoothing kernel to make gaussian blur
    # this reduce noise. Improves edge detection.
    smoothed = cv2.GaussianBlur(gray, (9,9), cv2.BORDER_DEFAULT)

    # threshold
    thresh = cv2.threshold(smoothed, 80, 255, cv2.THRESH_BINARY)[1]

    # compute Canny edge detection
    edges = cv2.Canny(thresh, 75, 150, apertureSize=3)

    # apply dialtion to highlight circlular areas.
    dilation = cv2.dilate(edges, np.ones((2,2)), iterations=2)

    keypoints = detector.detect(dilation)
    points = cv2.KeyPoint.convert(keypoints)
    
    if points is not None:
        x,y = points[0]
        r,g,b = img[int(x),int(y)]/255
        print(r)

    res = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    

    return res#cv2.hconcat([thresh, dilation, res])



