# Libraries used:
import cv2
import winsound

cam = cv2.VideoCapture(0)   # Capture video from webcam

while cam.isOpened():   # While loop to capture frames


    ret, frame1 = cam.read()    # Capture frame by frame 
    ret, frame2 = cam.read()    # Capture frame by frame 

    diff = cv2.absdiff(frame1, frame2)  # Find the difference between the two frames

    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)  # Convert the difference to grayscale

    blur = cv2.GaussianBlur(gray, (5, 5), 0)    # Blur the gray image

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)    # Threshold the image

    dilated = cv2.dilate(thresh, None, iterations=3)    # Dilate the image

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)    # Find the contours of the thresholded image

    for c in contours:    # Find the biggest contour (if detected)

        if cv2.contourArea(c) < 5000:        # Find the area of the contour
            continue
        x, y, w, h = cv2.boundingRect(c)        # Calculate the bounding box for the contour

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)        # Draw the rectangle around the contour

        winsound.Beep(500,200)        # Beep when the contour is detected

    if cv2.waitKey(10) == ord('q'):    # Close the camera when 'q' is pressed
        break
    cv2.imshow("cam-test", frame1)    # Display the resulting frame

