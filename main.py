import streamlit as st
import cv2
import numpy as np

st.title("Face Detection & Blurring App")

# load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def process_img(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        img[y:y+h, x:x+w] = cv2.blur(img[y:y+h, x:x+w], (30, 30))

    return img


uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)

    result = process_img(img)

    st.image(result, channels="BGR", caption="Blurred Image")
