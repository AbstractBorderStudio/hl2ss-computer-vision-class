import os
import cv2
import numpy as np

# Path to the folder containing your images
image_folder = 'C:/Users/danie/Documents/Personale/Università/Polito/Progetti/ComputerVision/hl2ss-computer-vision-class/viewer/output/imgs_long/ab'

# Get a list of image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")] #if #(not img.endswith("ab.pgm") and img.endswith(".pgm"))]

# Sort the image files by name if needed
images.sort()  # This will ensure the images are shown in order

# Open the first image to get its dimensions for the video window
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = first_image.shape

# Create a VideoWriter object to display the images
video = cv2.VideoWriter('ab_long.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height))

for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY)
    
    video.write(binary_image)
    
    cv2.imshow('Image Sequence', binary_image)


    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()