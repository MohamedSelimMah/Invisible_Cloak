# Invisible Cloak Using OpenCV

This project creates an "invisibility cloak" effect using a webcam and OpenCV. It detects a specific color (blue, in this version) and replaces it with the previously captured background, making objects of that color appear invisible in real-time.

---

## Demo
![Invisible Cloak Demo](https://via.placeholder.com/800x400?text=Demo+Image)  
*A real-time invisibility effect where blue objects disappear!*

---

## Features
- Real-time color detection and replacement.
- Adjustable color ranges for detecting different colors.
- Simple and user-friendly implementation using Python and OpenCV.

---

## How It Works
1. The program captures a background image when no object is in the frame.
2. It detects the specified color (blue by default) in the video stream using HSV color space.
3. The detected color areas are replaced with the captured background to create an "invisibility" effect.

---

## Installation
### Prerequisites
- Python 3.6 or later
- OpenCV library
- NumPy library

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/invisible-cloak.git
   cd invisible-cloak
