import cv2
import numpy as np
from matplotlib import pyplot as plt
from enum import Enum

class Blob:
    """
    BlobDetection API for Computer Vision. 
    """

    class Config(Enum):
        HOUGHCIRCLE = 0,
        SIMPLE_BLOB = 1,
        CANNY = 2,
        SOBEL = 3
    
    # ========= HOUGHCIRCLE CONFIGURATION ========= #
    # Gaussian blur kernel
    sm_kernel_size = 3 # (3,9,15,...3*k)
    
    # Colorspace Thresholding
    th_thresh = (80,255) # (threshold_1,threshold_2) 
    
    # Canny Edge Detection
    edge_thresh = (160,80) # (threshold_1,threshold_2)
    
    # Dilation kernel
    d_kernel_size = 3 
    # ============================================= #

    # ==== SIMPLE BLOB DETECTION CONFIGURATION ==== #
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 20 #20
    params.maxThreshold = 200 #200

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1 #0.5

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.9 #0.8

    # Filter by Inertia
    params.filterByInertia = True #True
    params.minInertiaRatio = 0.1 #0.1

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    # ============================================= #

    def FindCirclesFine(
            img, 
            applyGray=True, 
            applyBlur=True, 
            applyThresh=True,
            applyEdge=True,
            applyMorph=True,
            marker_color=(0,255,0),
            showPasses=False,
            edgeMethod=Config.CANNY,
            blobMethod=Config.HOUGHCIRCLE):
        """
        # Description

        Blob detection using cv2.HoughCircles. The frame is processed 
        to enhance information.

        1. convert to grayscale
        2. apply gaussian blur kernel to reduce noise
        3. thresholding
            2.1 this is useful if the image src has an high contrast 
                between background and foreground
        4. apply edge detecion
            4.1 remove complexity
            4.2 isolate only blob area
        5. apply morphological operators
            5.1 use a dilate function to reduce/remove gaps in circles
        6. apply HoughCircles to find circles

        # Variables

        - img: 
            - frame to analize
        - applyGray (True): 
            - allow/skip grayscale convertion pass 
        - applyBlur (True): 
            - allow/skip blur pass 
        - applyThresh (True): 
            - allow/skip thresholding pass
        - applyEdge (True): 
            - allow/skip edgedetection pass
        - applyMorph (True): 
            - allow/skip morphing operator pass
        - marker_color (0,255,0):
            - set marker color
        - showPasses (False): 
            - if ture return concatenated passes of the image pre-processing
        - edgeMethod (Config.CANNY/Config.SOBEL): 
            - select edge detection algorithm 
        - blobMethod (Config.HOUGHCIRCLE/Config.SIMPLE_BLOB): 
            - select blob detection algorithm 
        """

        # reference to frame
        res = img

        # grayscale image
        if applyGray:
            gray = res = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # increase contrast via equalization
        #eq = cv2.equalizeHist(gray)

        # Apply a smoothing kernel to make gaussian blur
        # this reduce noise. Improves edge detection.
        if applyBlur:
            blur = res = cv2.GaussianBlur(res, (Blob.sm_kernel_size,Blob.sm_kernel_size), cv2.BORDER_DEFAULT)

        # threshold
        if applyThresh:
            thresh = res = cv2.threshold(res, Blob.th_thresh[0], Blob.th_thresh[1], cv2.THRESH_BINARY)[1]

        # compute Canny edge detection
        if applyEdge:
            if edgeMethod == Blob.Config.CANNY:
                edge = res = cv2.Canny(res, Blob.edge_thresh[0], Blob.edge_thresh[1], apertureSize=3)
            elif edgeMethod == Blob.Config.SOBEL:
                edge = res = cv2.Sobel(src=res, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

        # apply dialtion to highlight circlular areas.
        if applyMorph:
            morph = res = cv2.dilate(res, np.ones((Blob.d_kernel_size,Blob.d_kernel_size)), iterations=1)

        if blobMethod == Blob.Config.HOUGHCIRCLE:
            # apply hough transform to detect circles
            circles = cv2.HoughCircles(res, cv2.HOUGH_GRADIENT_ALT, dp=1.5, minDist=25, param1=150, param2=0.1, minRadius=2, maxRadius=100)
            # add circles to 
            
            if circles is not None:
                for circle in circles[0,:]:
                    x, y, r = circle
                    center = (int(x), int(y))
                    cv2.circle(img, center, int(r), marker_color, cv2.FILLED) # add cv2.FILLED to fill the circle 
            return img, circles
        elif blobMethod == Blob.Config.SIMPLE_BLOB:
            keypoints = Blob.detector.detect(res)

            if keypoints is not None:
                points = cv2.KeyPoint.convert(keypoints)
                # if np.size(points) > 0:
                #     x,y = points[0]
                #     r,g,b = img[int(x),int(y)]/255
                #     print(r)

                img = cv2.drawKeypoints(img, keypoints, np.array([]), marker_color, cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
            
            return img, keypoints

        """
        return cv2.hconcat([edge, morph, img]) to show
        image processing passes.

        return img to only show the finale result. 
        """
        if showPasses:   
            return cv2.hconcat([edge, morph, img])
        return img, None




# =========== simple blob detection param initialization ===========





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

    if keypoints is not None:
        points = cv2.KeyPoint.convert(keypoints)
        if np.size(points) > 0:
            x,y = points[0]
            r,g,b = img[int(x),int(y)]/255
            print(r)

        res = cv2.drawKeypoints(gray, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    else:
        res = gray

    return res#cv2.hconcat([thresh, dilation, res])



