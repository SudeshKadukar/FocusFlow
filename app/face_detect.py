import cv2
import time
import os
from gtts import gTTS # New Marathi Voice Library

# 1. SETUP: Create Voice File
voice_file = "marathi_alert.mp3"
if not os.path.exists(voice_file):
    print("Generating Marathi Voice...")
    tts = gTTS(text="डोळे बघ डोळे बघ", lang='mr')
    tts.save(voice_file)

if not os.path.exists('distractions'):
    os.makedirs('distractions')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

distracted_start_time = 0
is_distracted = False
photo_taken = False

while True:
    ret, frame = cap.read()
    if not ret: break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) > 0:
        status, color = "FOCUSED", (0, 255, 0)
        is_distracted, photo_taken = False, False
    else:
        status, color = "DISTRACTED!", (0, 0, 255)
        if not is_distracted:
            distracted_start_time = time.time()
            is_distracted = True
        
        away_duration = int(time.time() - distracted_start_time)
        cv2.putText(frame, f"Away for: {away_duration}s", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # 2. MARATHI VOICE ALERT: After 5 seconds
        if away_duration >= 5:
            # Play the Marathi sound file using Windows system player
            os.system(f"start /min {voice_file}") 
            
            if not photo_taken:
                cv2.imwrite(f"distractions/evidence_{int(time.time())}.jpg", frame)
                photo_taken = True

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

    cv2.putText(frame, f"STATUS: {status}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow('AI Study Assistant', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()