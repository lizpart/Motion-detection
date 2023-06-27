# Motion-detection

Importing the necessary libraries: The code imports OpenCV (cv2), NumPy (np), datetime, and imutils.

Video capture: The code creates a VideoCapture object to access the camera.

Reading initial frames: Two frames, mapping1 and mapping2, are read from the video capture object.

Motion detection loop: The main loop of the program starts. It performs the following steps:

a. Calculating the absolute difference between mapping1 and mapping2 frames using the absdiff function.

b. Converting the difference frame to grayscale using cvtColor and then applying Gaussian blur using GaussianBlur.

c. Thresholding the blurred frame to create a binary image using the threshold function.

d. Dilating the thresholded image to fill in the holes and improve the contours using dilate.

e. Finding contours in the dilated image using findContours.

f. Processing each contour:

Checking the area of the contour. If it is smaller than 700, it is likely noise, so it is skipped.

Drawing a rectangle around the contour on the mapping1 frame using rectangle.

Adding text to indicate that motion has been detected on the mapping1 frame using putText.

Adding a timestamp on the mapping1 frame using putText and datetime.datetime.now().

g. Displaying the frames: The mapping1 frame, thresholded frame, and difference frame are displayed using imshow.

h. Updating the frames: The current mapping2 frame is assigned to mapping1, and a new frame is read into mapping2.

i. Exiting the program: If the user presses the "q" key, the program breaks out of the loop.

Cleaning up: After the loop ends, OpenCV windows are closed and resources are released using destroyAllWindows.

Note: The code assumes that you have a camera connected to your system and that it is accessible through OpenCV.
