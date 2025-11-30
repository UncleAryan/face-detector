# Face Detector 👤

A real-time face detection application built with Python and OpenCV. This program uses your webcam to detect faces in real-time and draws bounding boxes around them.

## Features ✨

- Real-time face detection from webcam feed
- Simple and intuitive interface
- Red bounding boxes around detected faces
- Face counter display
- Easy to use and modify

## Installation 🛠️

### Prerequisites
- Python 3.6 or higher
- Webcam

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/face-detector.git
cd face-detector
```

### Step 2: Install Dependencies
```bash
pip install opencv-python
```

### Step 3: Download Cascade File
The program requires the ```haarcascade_frontalface_default.xml``` file. If you clone this repository, it should be there.

## Usage 🚀

### Running the Program

```bash
python face-detector.py
```

### Controls
- The program will open a window showing your webcam feed
- Faces will be highlighted with blue bounding boxes (this can be changed by modifying the RGB values for the rectangle)
- The number of detected faces is displayed in the top-left corner
- Press 'q' to quit the application

## How It Works 🔍

This application uses OpenCV's Haar Cascade classifier for face detection:
1. Video Capture: Accesses your webcam feed
2. Pre-processing: Converts frames to grayscale for faster processing
3. Face Detection: Uses the Haar Cascade classifier to detect faces
4. Visualization: Draws bounding boxes around detected faces
5. Display: Shows the processed video feed in real-time

## Project Structure 📁
```
face-detector/
├── face-detector.py                     # Main application file
├── haarcascade_frontalface_default.xml  # Face detection classifier
├── README.md                            # Project documentation
```

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

### Third-Party Components
- The `haarcascade_frontalface_default.xml` file is part of OpenCV and is distributed under the Intel License Agreement.
- OpenCV is licensed under the 3-clause BSD License.
