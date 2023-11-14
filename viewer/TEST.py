import hl2ss_3dcv as h3d
import cv2
from matplotlib import pyplot as plt

ROTATE_RF = 2
ROTATE_LF = 0

rf_path = "output/stereo/src/rf/rf_frame5.png"
rf_image = cv2.imread(rf_path, cv2.IMREAD_UNCHANGED)
rf_rot = h3d.rm_vlc_rotate_image(rf_image, ROTATE_RF)

lf_path = "output/stereo/src/lf/lf_frame5.png"
lf_image = cv2.imread(lf_path, cv2.IMREAD_UNCHANGED)
lf_rot = h3d.rm_vlc_rotate_image(lf_image, ROTATE_LF)

rf_res = cv2.cvtColor(rf_rot, cv2.COLOR_BGR2RGB)
lf_res = cv2.cvtColor(lf_rot, cv2.COLOR_BGR2RGB)

plt.subplot(121), plt.title("lf"), plt.axis(False)
plt.imshow(lf_res)
plt.subplot(122), plt.title("rf"), plt.axis(False)
plt.imshow(rf_res)

plt.show()