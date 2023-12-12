import numpy as np
import cv2
import glob

#criteri di terminazione
#in questo caso si ferma dopo 30 iterazioni o se la precisione è maggiore di 0.001
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

#preparazione object points, come (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

#definiamo dei vettori per salvare i punti dell'oggetto e i punti dell'immagine da tutte le immagini
objpoints = [] #punti 3d nell spazio del mondo reale
imgpoints = [] #punti 2d nel piano dell'immagine

path = ''
images = glob.glob('')