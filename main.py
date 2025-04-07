import cv2 as cv
# import mediapipe as mp

capture = cv.VideoCapture(0)

while True:
    ret,frame = capture.read()
    if not ret:
        break

    # Show the captured frame in a window
    cv.imshow("Webcam", frame)

    # Exit loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
capture.release()
cv.destroyAllWindows()