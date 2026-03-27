# 🔐 Real-Time Face Unlock System

A real-time face recognition based authentication system built as a Final Year BTech CSE (Data Science & AIML) project.

---

## 📌 Project Overview

This system uses computer vision and deep learning to recognize faces in real-time via webcam. It can register multiple users, unlock access based on face recognition, and maintain a complete access log with timestamps.

---

## ✨ Features

- 📸 **Face Registration** — Register multiple users via webcam
- 🔓 **Real-Time Face Unlock** — Recognize faces instantly using webcam
- 📊 **Confidence Score** — Shows match confidence percentage for each recognition
- 👥 **Multiple User Support** — Register and manage multiple faces
- 📋 **Access Logs** — Every unlock attempt is saved with timestamp to CSV
- 🗑️ **Delete Users** — Remove registered users from the system
- 🖥️ **Clean Menu Interface** — Easy to use terminal-based menu

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Core programming language |
| OpenCV | Webcam access and video processing |
| face_recognition | Face detection and encoding |
| dlib | Deep learning face recognition models |
| NumPy | Array and image processing |
| Pickle | Saving and loading face encodings |
| CSV | Access log storage |

---

## 📁 Project Structure
```
Face_unlock_system/
│
├── src/
│   ├── main.py              # Main menu interface
│   ├── register_face.py     # Face registration system
│   └── unlock.py            # Face unlock/recognition system
│
├── data/
│   └── access_log.csv       # Auto-generated access logs
│
├── models/
│   └── faces.pkl            # Saved face encodings
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/MohitXGandhi/face-unlock-system.git
cd face-unlock-system
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dlib (pre-built wheel for Python 3.11)
```bash
pip install https://github.com/z-mahmud22/Dlib_Windows_Python3.x/raw/main/dlib-19.24.1-cp311-cp311-win_amd64.whl
```

### 4. Install remaining dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the main menu:
```bash
python src/main.py
```

### Menu Options:
| Option | Description |
|--------|-------------|
| 1 | Register a new face |
| 2 | Launch face unlock |
| 3 | List registered users |
| 4 | Delete a user |
| 5 | View access logs |
| 6 | Exit |

---

## 🧠 How It Works

1. **Registration** — Webcam captures your face, converts it to a 128-dimension face encoding using dlib's deep learning model, and saves it to `models/faces.pkl`
2. **Recognition** — Live webcam feed is compared frame by frame against saved encodings using Euclidean distance
3. **Decision** — If distance is below threshold (0.5), access is granted with confidence score
4. **Logging** — Every attempt is logged to `data/access_log.csv` with timestamp

---

## 👨‍💻 Author

**Mohit Gandhi**
BTech CSE (Data Science & AIML)