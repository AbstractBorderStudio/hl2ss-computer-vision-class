import cv2
import matplotlib.pyplot as plt


def grab_frame(cap):
    """
    Method to grab a frame from the camera
    :param cap: the VideoCapture object
    :return: the captured image
    """
    ret, frame = cap.read()
    return frame


def handle_close(event, cap):
    """
    Handle the close event of the Matplotlib window by closing the camera capture
    :param event: the close event
    :param cap: the VideoCapture object to be closed
    """
    cap.release()


def bgr_to_gray(image):
    """
    Convert a BGR image into grayscale
    :param image: the BGR image
    :return: the same image but in grayscale
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def main():
    # init the camera
    cap = cv2.VideoCapture(0)

    # enable Matplotlib interactive mode
    plt.ion()

    # create a figure to be updated
    fig = plt.figure()
    fig.canvas.mpl_connect("close_event", lambda event: handle_close(event, cap))

    # prep a variable for the first run
    ax_img = None

    while cap.isOpened():
        # get the current frame
        frame = grab_frame(cap)
        frame = frame[:,::-1] # mirror frame

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        canny = cv2.Canny(frame, .1, .3)

        # apply sobel
        x = cv2.Sobel(frame, cv2.CV_16S, 1, 0, ksize=3)
        y = cv2.Sobel(frame, cv2.CV_16S, 0, 1, ksize=3)

        frame_sobel = cv2.addWeighted(x,0.5,y,0.5,0.0)

        if ax_img is None:
            # convert the current (first) frame in grayscale
            # ax_img = plt.imshow(frame_sobel, cmap='gray', vmin=0, vmax=255)#)bgr_to_gray(canny), "gray")
            # plt.axis("off")  # hide axis, ticks, ...
            # plt.title("Camera Capture")

            ax_img = plt.imshow(frame_sobel, cmap='gray', vmin=0, vmax=255)#)bgr_to_gray(canny), "gray")
            plt.axis("off")
            
            # show the plot!
            plt.show()
        else:
            # set the current frame as the data to show
            ax_img.set_data(frame_sobel)#bgr_to_gray(canny))
            # update the figure associated to the shown plot
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(1/30)  # pause: 30 frames per second


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)