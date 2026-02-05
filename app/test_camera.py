import cv2

# Start the camera
cap = cv2.VideoCapture(0)

print("Camera is starting... Look at the lens!")
print("Press 'q' on your keyboard to close the window.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Camera not found.")
        break

    # Show the video feed
    cv2.imshow('AI Study Assistant Test', frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 