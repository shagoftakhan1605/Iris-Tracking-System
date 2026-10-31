import cv2
import mediapipe as mp
import math
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Indices for iris landmarks in the Face Mesh model
LEFT_IRIS = [474, 475, 476, 477]  # Left iris landmarks
RIGHT_IRIS = [469, 470, 471, 472]  # Right iris landmarks

LEFT_EYE = [33, 133, 160, 159, 158, 144, 153, 154, 155, 246]
RIGHT_EYE = [362, 263, 387, 386, 385, 373, 380, 381, 382, 466]

# Eye corner landmarks that belong to each iris (inner and outer corner)
LEFT_IRIS_CORNERS = [362, 263]   # same eye as LEFT_IRIS (474-477)
RIGHT_IRIS_CORNERS = [33, 133]   # same eye as RIGHT_IRIS (469-472)

def relative_iris_position(center, corner_points):
    """Horizontal iris position inside the eye: 0 = image-left corner, 1 = image-right corner."""
    left_x = min(pt[0] for pt in corner_points)
    right_x = max(pt[0] for pt in corner_points)
    eye_width = right_x - left_x
    if eye_width == 0:
        return 0.5
    return (center[0] - left_x) / eye_width

def calculate_angle(relative_position):
    """Classify gaze direction and give an approximate angle from the relative iris position.
    Directions are in image coordinates (the webcam image is not mirrored)."""

    # Determine the gaze direction based on the relative position
    if relative_position < 0.4:
        direction = "Looking Left"
    elif relative_position > 0.6:
        direction = "Looking Right"
    else:
        direction = "Looking Center"

    # Approximate gaze angle: a linear mapping, not a calibrated measurement
    angle = (relative_position - 0.5) * 60  # Assuming maximum angle of +/- 30 degrees

    return direction, angle

def process_frame(frame, face_mesh):
    """Process each frame to detect gaze direction."""
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Draw the face mesh landmarks
            mp_drawing.draw_landmarks(
                image=frame,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())

            # Extract iris and eye landmarks
            left_iris_landmarks = [(int(face_landmarks.landmark[idx].x * frame.shape[1]), 
                                    int(face_landmarks.landmark[idx].y * frame.shape[0])) for idx in LEFT_IRIS]
            right_iris_landmarks = [(int(face_landmarks.landmark[idx].x * frame.shape[1]), 
                                     int(face_landmarks.landmark[idx].y * frame.shape[0])) for idx in RIGHT_IRIS]

            left_eye_landmarks = [(int(face_landmarks.landmark[idx].x * frame.shape[1]), 
                                   int(face_landmarks.landmark[idx].y * frame.shape[0])) for idx in LEFT_EYE]
            right_eye_landmarks = [(int(face_landmarks.landmark[idx].x * frame.shape[1]), 
                                    int(face_landmarks.landmark[idx].y * frame.shape[0])) for idx in RIGHT_EYE]

            # Calculate the center of the iris
            left_iris_center = (
                int(sum([pt[0] for pt in left_iris_landmarks]) / len(left_iris_landmarks)),
                int(sum([pt[1] for pt in left_iris_landmarks]) / len(left_iris_landmarks))
            )
            right_iris_center = (
                int(sum([pt[0] for pt in right_iris_landmarks]) / len(right_iris_landmarks)),
                int(sum([pt[1] for pt in right_iris_landmarks]) / len(right_iris_landmarks))
            )



            # Draw circles around the iris centers
            cv2.circle(frame, left_iris_center, 10, (0, 255, 0), 2)
            cv2.circle(frame, right_iris_center, 10, (0, 255, 0), 2)

            # Gaze estimate: average the relative iris position of both eyes
            def to_px(idx):
                lm = face_landmarks.landmark[idx]
                return (int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0]))
            rel_left = relative_iris_position(left_iris_center, [to_px(i) for i in LEFT_IRIS_CORNERS])
            rel_right = relative_iris_position(right_iris_center, [to_px(i) for i in RIGHT_IRIS_CORNERS])
            direction, angle = calculate_angle((rel_left + rel_right) / 2)
            cv2.putText(frame, f"{direction} ({angle:.1f} deg, approx.)", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    return frame

def start_real_time_tracking():
    """Start the real-time tracking using webcam."""
    cap = cv2.VideoCapture(0)
    with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = process_frame(frame, face_mesh)
            
            # Display the resulting frame
            cv2.imshow('Iris Tracker', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def upload_video():
    """Process an uploaded video file."""
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
    if not video_path:
        messagebox.showwarning("No file selected", "Please select a video file.")
        return

    cap = cv2.VideoCapture(video_path)
    with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5) as face_mesh:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = process_frame(frame, face_mesh)
            
            # Display the resulting frame
            cv2.imshow('Iris Tracker', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def create_gui():
    """Create the GUI to choose between real-time tracking and video processing."""
    root = tk.Tk()
    root.title("Iris Tracking System")

    tk.Label(root, text="Choose an option:", font=("Arial", 14)).pack(pady=10)

    tk.Button(root, text="Real-Time Tracking", font=("Arial", 12), command=start_real_time_tracking).pack(pady=10)
    tk.Button(root, text="Upload Video", font=("Arial", 12), command=upload_video).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
