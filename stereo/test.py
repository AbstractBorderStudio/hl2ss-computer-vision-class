import ..viewer.hl2ss_3dcv as h3d
import cv2

path = '/viewer/output/stereo/src/lf/lf_frame0.png'

image = cv2.imread(path, cv2.IMREAD_UNCHANGED)

res = h3d.rm_vlc_rotate_image(image, 90)

cv2.imshow("res", res)
cv2.waitKey(0)
cv2.destroyAllWindows()