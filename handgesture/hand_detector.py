#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import cv2
import mediapipe as mp

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_hands(self, img):
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    img, hand, self.mp_hands.HAND_CONNECTIONS
                )
        return img

    def find_positions(self, img):
        lm_list = []
        if self.results and self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            h, w, _ = img.shape
            for idx, lm in enumerate(hand.landmark):
                lm_list.append([idx, int(lm.x*w), int(lm.y*h)])
        return lm_list



# In[ ]:





