import os
import cv2
import numpy as np
import Project.segmentation

# Path to the folder containing your images
image_folder = 'imgs_long/ab'

# Get a list of image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith('.png')]#(not img.endswith("ab.pgm") and img.endswith(".png"))]

# Sort the image files by name if needed
images.sort()  # This will ensure the images are shown in order

# Open the first image to get its dimensions for the video window
#first_image = cv2.imread(os.path.join(image_folder, images[0]))
#height, width, layers = first_image.shape

# Create a VideoWriter object to display the images
#video = cv2.VideoWriter('ab_long.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height))

for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)

    # apply edge 
    circle = Project.segmentation.FindCirclesSimpleBlob(frame)
    circle2 = Project.segmentation.FindCirclesFine(frame)

    #video.write(circle)

    # show result
    cv2.imshow('simple blob detection', circle)
    cv2.imshow('custom blob detection', circle2)

    # Break the loop if the user presses the 'q'q key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

#video.release()
cv2.destroyAllWindows()