import cv2
import streamlit as st
import numpy as np

st.title("Webcam and Image Processing")


run_webcam = st.checkbox("Run Webcam")
FRAME_WINDOW = st.image([])

uploaded_file = st.file_uploader("Choose an Image", type=["jpg", "png", "jpeg"])
image_container = st.empty()

camera = cv2.VideoCapture(0)

def process_image(image):
  if image.ndim == 3 and image.shape[2] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  return image

while run_webcam:
  _, frame = camera.read()
  frame = process_image(frame)
  FRAME_WINDOW.image(frame)

  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()

if uploaded_file is not None:
  image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
  image = process_image(image)
  image_container.image(image, caption="Uploaded Image")
