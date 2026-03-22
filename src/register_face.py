import face_recognition
import cv2
import pickle
import os
import numpy as np

ENCODINGS_PATH = "models/faces.pkl"

def load_existing_data():
    if os.path.exists(ENCODINGS_PATH):
        with open(ENCODINGS_PATH, "rb") as f:
            return pickle.load(f)
    return {"names": [], "encodings": []}

def register_face():
    print("\n📸 Face Registration System")
    print("----------------------------")
    name = input("Enter your name: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    print(f"\n✅ Hello {name}! Opening webcam...")
    print("👉 Press SPACE to capture your face | Press Q to quit\n")

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ Could not open webcam.")
        return

    for i in range(10):
        cap.read()

    captured_encoding = None

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("❌ Failed to read from webcam.")
            break

        cv2.putText(frame, "Press SPACE to capture | Q to quit",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Register Face", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("⚠️ Registration cancelled.")
            break

        elif key == ord(' '):
            print("📷 Capturing face...")
            frame_uint8 = np.array(frame, dtype=np.uint8)
            rgb_frame = cv2.cvtColor(frame_uint8, cv2.COLOR_BGR2RGB)
            rgb_frame = np.ascontiguousarray(rgb_frame, dtype=np.uint8)
            print(f"Frame shape: {rgb_frame.shape}, dtype: {rgb_frame.dtype}")
            face_locations = face_recognition.face_locations(rgb_frame)

            if len(face_locations) == 0:
                print("❌ No face detected. Please try again.")
                continue

            if len(face_locations) > 1:
                print("⚠️ Multiple faces detected.")
                continue

            encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            captured_encoding = encoding
            print(f"✅ Face captured successfully for '{name}'!")
            break

    cap.release()
    cv2.destroyAllWindows()

    if captured_encoding is not None:
        data = load_existing_data()
        data["names"].append(name)
        data["encodings"].append(captured_encoding)
        os.makedirs("models", exist_ok=True)
        with open(ENCODINGS_PATH, "wb") as f:
            pickle.dump(data, f)
        print(f"\n🎉 '{name}' registered successfully!")
        print(f"📁 Saved to: {ENCODINGS_PATH}")
    else:
        print("\n❌ Registration failed. No face was saved.")

if __name__ == "__main__":
    register_face()