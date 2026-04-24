Face Detection & Blurring Project
📌 Overview

This project uses Computer Vision with OpenCV to detect human faces in images or video streams and automatically blur them. It can be used for privacy protection, surveillance systems, or anonymizing datasets.

🚀 Features
Detects faces in real-time using webcam or images
Applies blur effect to detected faces
Supports both image and video processing
Fast and efficient using Haar Cascade classifier
🛠️ Tech Stack
Python 🐍
OpenCV
NumPy
⚙️ Installation
Clone the repository:
git clone https://github.com/your-username/face-detection-blur.git
cd face-detection-blur
Install dependencies:
pip install opencv-python numpy
▶️ Usage
🔹 For Image
python face_blur.py --image path/to/image.jpg
🔹 For Webcam (Real-Time)
python face_blur.py --webcam
🧠 How It Works
Loads pre-trained Haar Cascade model
Converts image to grayscale
Detects faces using detectMultiScale()
Applies Gaussian Blur to detected regions
Displays or saves the output
🖼️ Output
Faces in the image/video are automatically blurred

Output is shown in a window or saved in the output folder
🔐 Use Cases
Privacy protection

CCTV footage anonymization

Social media content masking

Dataset preprocessing
📌 Future Improvements

Use Deep Learning (DNN / YOLO) for better accuracy

Add face recognition + selective blurring

Blur other objects (license plates, etc.)
🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss.

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Piyush Kumar
