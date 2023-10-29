import cv2 
import numpy as np
import os
from matplotlib import pyplot as plt
from enum import Enum
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.morphology import *
from skimage.measure import label, regionprops



sample = cv2.imread('frame0.png')

sample_g = gray = cv2.cvtColor(sample, cv2.COLOR_BGR2GRAY)


fig, ax = plt.subplots(1,2,figsize=(10,5))
ax[0].imshow(sample)
ax[1].imshow(sample_g,cmap='gray')
ax[0].set_title('Colored Image',fontsize=15)
ax[1].set_title('Grayscale Image',fontsize=15)
plt.show()

#serve per binarizzare l'immagine, bisogna scegliere l'opportuno livello oltre cui si accetta il bianco diciamo così, io l'ho scelto in base al plot
#saple g [250 perchè è la metà dell'immagine]
ig, ax = plt.subplots(1,3,figsize=(15,5))
sample_b = sample_g >80
ax[0].set_title('Grayscale Image',fontsize=20)
ax[0].imshow(sample_g,cmap='gray')
ax[1].plot(sample_g[250])
ax[1].set_ylabel('Pixel Value')
ax[1].set_xlabel('Width of Picture')
ax[1].set_title('Plot of 1 Line',fontsize=15)
ax[2].set_title('Binarized Image',fontsize=15)
ax[2].imshow(sample_b,cmap='gray')

plt.show()




fig, ax = plt.subplots(1,4,figsize=(10,5))
ax[0].set_title('Binarized Image',fontsize=15)
ax[0].imshow(sample_g,cmap='gray')
#a blob log necessario passare l'immagine, poi la massima dimensione dei cerchi in pixel, threshol 
# I blob con un'intensità superiore alla soglia vengono rilevati, mentre quelli con un'intensità inferiore non vengono considerati
blobs = blob_log(sample_b, max_sigma=25, threshold=0.67)
ax[1].imshow(sample_b, cmap='gray')
for blob in blobs:
    y, x, area = blob
    ax[1].add_patch(plt.Circle((x, y), area*np.sqrt(2), color='r', 
                            fill=False))
ax[1].set_title('Using LOG',fontsize=15)

blobs = blob_dog(sample_b, max_sigma=40, threshold=0.4)
ax[2].imshow(sample_b, cmap='gray')
for blob in blobs:
    y, x, area = blob
    ax[2].add_patch(plt.Circle((x, y), area*np.sqrt(2), color='b', 
                            fill=False))
ax[2].set_title('Using DOG',fontsize=15)

blobs = blob_doh(sample_b, max_sigma=35, threshold=0.06)
ax[3].imshow(sample_b, cmap='gray')
for blob in blobs:
    y, x, area = blob
    ax[3].add_patch(plt.Circle((x, y), area*np.sqrt(2), color='g', 
                            fill=False))
ax[3].set_title('Using DOh',fontsize=15)
plt.tight_layout()
plt.show()

#metodo che usa labelling

#sample_d = dilation(sample_b)
#sample_c = erosion(sample_d)
#sample_l = label(sample_c)
#sample_rp= regionprops(sample_l)

#print('How many Blobs detected?:', len(sample_rp))


#list1 = []
#for x in sample_rp:
#    list1.append(x.area)
#list2  = sorted(list(enumerate(list1)),key=lambda x: x[1], reverse=True)[:7]
#fig, ax = plt.subplots(1,4,figsize=(15,10))
#ax[0].imshow(sample_l)
#ax[0].set_title('Labelled Image',fontsize=15)
#for x,y in enumerate(list2[:3]):
#    ax[x+1].imshow(sample_rp[y[0]].image)
#    ax[x+1].set_title('Biggest Blob'+str(x+1))
#plt.show()






