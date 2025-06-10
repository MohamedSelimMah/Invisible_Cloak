# 🧙‍♂️ Invisible Cloak Using OpenCV 🪄

This project creates a magical "invisibility cloak" effect using a webcam and OpenCV. It detects a specific color (🔵 blue by default) and replaces it with the captured background, making objects of that color disappear in real-time. ✨

---

👀 *A real-time invisibility effect where blue objects vanish!*

---

## 🚀 Features

* ⚡ Real-time color detection and replacement.
* 🎨 Adjustable color ranges for detecting different colors.
* 🛠️ Simple and user-friendly implementation using Python and OpenCV.

---

## 🛡️ How It Works

1. 📸 The program captures a background image when no object is in the frame.
2. 🎯 It detects the specified color (🔵 blue by default) in the video stream using HSV color space.
3. 🪄 The detected color areas are replaced with the captured background to create an "invisibility" effect.

---

## 📥 Installation

### 📋 Prerequisites

* 🐍 Python 3.6 or later
* 🖼️ OpenCV library
* 🔢 NumPy library

### 🛠️ Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/invisible-cloak.git
   cd invisible-cloak
   ```
2. Install dependencies:

   ```bash
   pip install opencv-python numpy
   ```
3. Run the program:

   ```bash
   python invisible_cloak.py
   ```

---

## 🧑‍💻 Usage

1. 🎥 Ensure your webcam is connected.
2. 🏞️ Run the script and move out of the frame to capture the background.
3. 🔵 Wear or hold a blue object to watch it "disappear"! 💨

---

## ✏️ Customization

### 🎨 Change the Cloak Color

To change the detected color, modify the HSV range in the `main()` function:

```python
lower_blue = np.array([90, 50, 50])  # Lower range for blue
upper_blue = np.array([130, 255, 255])  # Upper range for blue
```

🔧 Replace the values with the desired color's HSV range.

---

## 🤝 Contributing

Contributions are welcome! 🎉
Feel free to open issues or submit pull requests for improvements or new features. 🛠️

---


## 🙌 Acknowledgments

* ❤️ **OpenCV** for its amazing library.
* 🧙‍♂️ Inspired by Harry Potter's invisibility cloak! ✨

---
