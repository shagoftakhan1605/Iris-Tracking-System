# Iris Tracking and Simple Gaze Direction

A webcam or video app that finds both irises with MediaPipe Face Mesh, marks their centres, and gives a simple horizontal gaze estimate (left, centre or right) with an approximate angle. A small Tkinter window lets you choose between the webcam and a video file.

All code is in [`iris_tracking.py`](iris_tracking.py).

---

## Results

![GIFMaker_me](https://github.com/user-attachments/assets/56ac0803-5a15-4aa5-a1a7-57dad1d95041)

---

## How It Works

1. **Landmarks:** MediaPipe Face Mesh with `refine_landmarks=True` returns 478 face landmarks, including four points around each iris.
2. **Iris centre:** the mean of the four iris points for each eye. A green circle is drawn at each centre and the face mesh is drawn over the face.
3. **Relative position:** for each eye, the iris centre's horizontal position between the two eye corners, from 0 (image-left corner) to 1 (image-right corner). The two eyes are averaged.
4. **Direction:** below 0.4 is "Looking Left", above 0.6 is "Looking Right", otherwise "Looking Center". Directions refer to the image, which is not mirrored.
5. **Approximate angle:** `(position - 0.5) x 60`, i.e. a linear mapping to plus or minus 30 degrees. This is a rough indicator, not a calibrated gaze angle.

---

## How to Run

```bash
pip install -r requirements.txt
python iris_tracking.py
```

Choose **Real-Time Tracking** for the webcam or **Upload Video** for an `.mp4` or `.avi` file. Press `q` to stop.

---

## Fix in This Version

The gaze function existed but was never called, so no direction or angle was shown. It is now applied to every frame, using the eye corners that belong to each iris (landmarks 33/133 with iris 469-472, and 362/263 with iris 474-477), and the result is written on the video.

---

## Limitations

* Horizontal direction only; vertical gaze and head rotation are not taken into account
* Thresholds and the angle mapping are fixed and not calibrated per person or camera
* Not suitable for research-grade eye tracking without calibration and validation

---

## Tools

Python, MediaPipe, OpenCV, Tkinter
