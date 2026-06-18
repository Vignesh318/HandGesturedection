#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from pathlib import Path
from datetime import datetime

class GestureLogger:
    def __init__(self, filename="gesture_log.csv"):
        self.file = Path(filename)
        if not self.file.exists():
            with open(self.file, "w", newline="") as f:
                csv.writer(f).writerow(["Timestamp", "Gesture"])

    def log(self, gesture):
        with open(self.file, "a", newline="") as f:
            csv.writer(f).writerow([datetime.now(), gesture])


# In[ ]:




