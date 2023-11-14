import cv2
import numpy as np
from matplotlib import pyplot as plt

pv_path = 'video.mp4'
fl_path = 'video.mp4'
fr_path = 'video.mp4'

pv_video = cv2.VideoCapture(pv_path)
fl_video = cv2.VideoCapture(fl_path)
fr_video = cv2.VideoCapture(fr_path)

# ---

count = 0
success = True
# while success:
#     success,frame = video.read()
#     cv2.imwrite("frame%d.jpg" % count, frame)
#     count += 1
pv_success, pv_frame = pv_video.read()
fl_success, fl_frame = pv_video.read()
fr_success, fr_frame = pv_video.read()

res = cv2.hconcat([(pv_frame, fl_frame, fr_frame)])

plt.imshow(res)
plt.show()