import cv2
import numpy as np

cap = cv2.VideoCapture(0)
canvas = None

lower_color = np.array([110, 30, 130])
upper_color = np.array([130, 100, 255])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours and len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        if radius > 5:
            cv2.circle(canvas, (int(x), int(y)), 5, (255, 0, 0), -1)

    combined = cv2.add(frame, canvas)
    cv2.imshow("Virtual Drawing", combined)

    key = cv2.waitKey(10) & 0xFF
    print(f"Key pressed: {key}")
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()