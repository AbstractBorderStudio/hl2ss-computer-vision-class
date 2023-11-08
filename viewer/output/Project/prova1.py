from math import sqrt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from skimage.color import rgb2gray
import cv2 

import matplotlib.pyplot as plt
image = cv2.imread('frame0.png')


#image = data.hubble_deep_field()[0:500, 0:500]
image_gray = rgb2gray(image)

blobs_log = blob_log(image_gray, max_sigma=40, num_sigma=40, threshold=.1)

# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

blobs_dog = blob_dog(image_gray, max_sigma=100, threshold=.1)
blobs_dog[:, 2] = blobs_dog[:, 2] * sqrt(2)

blobs_doh = blob_doh(image_gray, max_sigma=100, threshold=.01)

blobs_list = [blobs_log, blobs_dog, blobs_doh]
colors = ['yellow', 'lime', 'red']
titles = ['Laplacian of Gaussian', 'Difference of Gaussian',
          'Determinant of Hessian']
sequence = zip(blobs_list, colors, titles)
print(sequence)
fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

for idx, (blobs, color, title) in enumerate(sequence):
    ax[idx].set_title(title)
    ax[idx].imshow(image)
    for blob in blobs:
        y, x, r = blob
        print(blob)
        c = plt.Circle((x, y), r, color=color, linewidth=2, fill=False)
        ax[idx].add_patch(c)
    ax[idx].set_axis_off()
plt.axhline(y=image.shape[0]//2, color='r', linewidth=2)
plt.axvline(x=image.shape[1]//2, color='r', linewidth=2)
plt.tight_layout()
plt.show()

print("AAA")
for circle in blobs:
                print(circle)
                x, y, r = circle    
                center = (int(y), int(x))
                result = cv2.circle(image, center, int(r), (255, 0,0), cv2.FILLED)


# display it
#cv2.imshow("IMAGE", img)
#cv2.imshow("THRESHOLD", thresh)
#cv2.imshow("BLOB", blobs)
cv2.line(image, (0, image.shape[0]//2), (image.shape[0]//2, image.shape[1]//2), (0, 0, 255), 2)
cv2.line(image, (image.shape[0]//2, 0), (image.shape[0]//2, image.shape[1]//2), (0, 0, 255), 2)

#result = cv2.circle(image, (int(image.shape[0]/2),int(image.shape[1]/2)), int(r), (255, 255,0), cv2.FILLED)
cv2.imshow("RESULT", result)
cv2.waitKey(0)
