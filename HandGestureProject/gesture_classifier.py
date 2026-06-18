class GestureClassifier:
    TIP_IDS = [4, 8, 12, 16, 20]

    def classify(self, lm_list):
        if not lm_list:
            return None, 0

        fingers = []
        fingers.append(1 if lm_list[4][1] > lm_list[3][1] else 0)

        for i in range(1, 5):
            fingers.append(
                1 if lm_list[self.TIP_IDS[i]][2] < lm_list[self.TIP_IDS[i]-2][2] else 0
            )

        count = fingers.count(1)

        names = {
            0: "Fist",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Open Palm"
        }

        return names.get(count, "Unknown"), count
