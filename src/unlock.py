import face_recognition
import cv2
import pickle
import os
import numpy as np

ENCODINGS_PATH = "models/faces.pkl"

def load_known_faces():
    """Load saved face encodings."""
    if not os.path.exists(ENCODINGS_PATH):
        print("❌ No registered faces found. Please run register_face.py first.")
        return None
    with open(ENCODINGS_PATH, "rb") as f:
        return pickle.load(f)

def unlock():
    print("\n🔐 Face Unlock System")
    print("----------------------")

    data = load_known_faces()
    if data is None:
        return

    known_encodings = data["encodings"]
    known_names = data["names"]
    print(f"✅ Loaded {len(known_names)} registered face(s): {', '.join(known_names)}")
    print("\n👁️  Looking at camera... Press Q to quit\n")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    for i in range(10):
        cap.read()

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("❌ Failed to read from webcam.")
            break

        frame_uint8 = np.array(frame, dtype=np.uint8)
        rgb_frame = cv2.cvtColor(frame_uint8, cv2.COLOR_BGR2RGB)
        rgb_frame = np.ascontiguousarray(rgb_frame, dtype=np.uint8)

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"
            color = (0, 0, 255)

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_names[best_match_index]
                    color = (0, 255, 0)

            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            if name != "Unknown":
                print(f"✅ Access Granted 🔓 - Welcome, {name}!")
            else:
                print("❌ Access Denied 🔒 - Unknown Person!")

        status = "Scanning..." if len(face_locations) == 0 else ""
        cv2.putText(frame, status, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, "Press Q to quit", (10, 460),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("Face Unlock System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("\n👋 System closed.")

if __name__ == "__main__":
    unlock()