# FocusFlow 🌊

**Developed by [Sudesh Kadukar](https://github.com/SudeshKadukar)**

FocusFlow is an AI-powered study companion that uses computer vision to monitor your focus levels. If the system detects you are distracted or drowsy, it triggers personalized alerts to keep you on track.

---

## ✨ Key Features
* **Real-time Face Detection**: Uses Haar Cascade Classifiers to track user presence.
* **Native Audio Nudges**: Plays `marathi_alert.mp3` when focus wavers, providing a familiar and effective reminder.
* **Emergency SMS System**: Automatically sends an alert to a designated guardian (e.g., +919420355509) if a significant distraction or emergency is detected.
* **Evidence Logging**: Saves time-stamped screenshots of distractions in the `/distractions` folder for later review.

## 📂 Project Structure
* **`app/face_detect.py`**: The main logic for monitoring focus and sending alerts.
* **`app/test_camera.py`**: Utility script to verify camera hardware.
* **`app/marathi_alert.mp3`**: Custom Marathi audio alert file.
* **`app/haarcascade_frontalface_default.xml`**: Pre-trained model for facial detection.
* **`/distractions`**: Directory where evidence images are stored.

## 🛠️ Requirements
* Python 3.x
* OpenCV (`opencv-python`)
* A working webcam

## 🚀 How to Run
1. **Verify Camera:**
   ```bash
   python app/test_camera.py
