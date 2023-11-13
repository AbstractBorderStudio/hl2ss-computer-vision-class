# cosa fare: 
#1. fare blob detection su un'immagine colorata
#2. provare a generalizzare su video mp4 rgb facendo loop frame
#3. integrare in segmentation (se risultato buono) 

#Devo convertire l'immagine in HSV che è lo spazio di colori più comodo per effettuare segmentazione sul colore

import cv2 
import numpy as np
from matplotlib import pyplot as plt
from mp4ToFrameConv import mp4Converter as mp4tf

videoPath = "cut_colored_h2.mp4"
framesPath = "Colored_frames"

#mp4tf.mp4ToPng(videoPath,framesPath)

#prova con un'immagine
image = cv2.imread(f"{framesPath}/frame23.png")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#scegliere lower ed upper bound del giallo -> attenzione: openCV non mappa la hue da 0 a 360 
# ma da 0 a 180 
lower_limit = np.array([20,100,100])
upper_limit = np.array([40,255,255])

#creiamo maschera per questo range di colori
mask = cv2.inRange(hsv_image, lower_limit, upper_limit)
# bounding box dall'immagine mascherata (da sostituire con  centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i]))
bbox = cv2.boundingRect(mask)
#center, radius = cv2.minEnclosingCircle(mask)

#in questo momento stampa solo un bounding box -> aggiungere ciclo
if bbox is not None:
    print("Object detected")
    x,y,w,h = bbox
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0),2)
else:
    print("Object not detected")
    
cv2.imshow('image', image)
cv2.waitKey(0)