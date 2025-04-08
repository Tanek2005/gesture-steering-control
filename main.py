import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get the frame dimensions
    height, width = frame.shape[:2]

    # Calculate the center based on frame size
    center = (width // 2, height // 2)

    radius = 1000
    color = (0, 255, 255)
    thickness = 2

    # Draw the circle in the center
    cv2.circle(frame, center, radius, color, thickness)

    # Show the frame with the circle
    cv2.imshow("Webcam with Centered Circle", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
