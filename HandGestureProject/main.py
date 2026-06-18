import cv2
from gesture_classifier import GestureClassifier
from hand_detector import HandDetector
from gesture_logger import GestureLogger
import mediapipe as mp

cap = cv2.VideoCapture(0)

detector = HandDetector()
classifier = GestureClassifier()
logger = GestureLogger()

last_gesture = None

while True:
    success, img = cap.read()
    if not success:
        break

    img = detector.find_hands(img)
    lm_list = detector.find_positions(img)

    gesture, count = classifier.classify(lm_list)

    if gesture:
        cv2.putText(img, f"Gesture: {gesture}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.putText(img, f"Fingers: {count}", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

        if gesture != last_gesture:
            logger.log(gesture)
            last_gesture = gesture

    cv2.imshow("Hand Gesture Recognition", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
