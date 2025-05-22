import cv2
import numpy as np

def capture_background(cap, num_frame=30):
    print("Please move out of the frame while capturing the background!!")
    bg = []
    for i in range(num_frame):
        ret, frame = cap.read()
        if ret:
            bg.append(frame)
    return np.median(bg, axis=0).astype(np.uint8)

def detect_color(frame, lower_b, upper_b):
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_b, upper_b)
    return cv2.dilate(cv2.morphologyEx(mask, cv2.MORPH_OPEN, None), None)

def become_invisible(frame, mask, background):
    inverse_mask = cv2.bitwise_not(mask)
    foreground = cv2.bitwise_and(frame, frame, mask=inverse_mask)
    background_part = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(foreground, background_part)

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Camera not detected!")
        return
    
    # Capture the background
    background = capture_background(cam)

    # Define the color range for blue
    lower_blue = np.array([90, 50, 50])   # Lower range for blue
    upper_blue = np.array([130, 255, 255])  # Upper range for blue

    print("Press 'q' to exit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Could not read the frame.")
            continue

        # Detect the blue color and apply the invisibility effect
        mask = detect_color(frame, lower_blue, upper_blue)
        result = become_invisible(frame, mask, background)

        # Display the result
        cv2.imshow("Invisible Cloak", result)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
