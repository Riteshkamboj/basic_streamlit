import cv2
import streamlit as st

st.title("Webcam Live Feed")

run = st.checkbox("Run")
FRAME_WINDOW = st.image([])

camera = cv2.VideoCapture(0)  # 0 is the default webcam

while run:
  _, frame = camera.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert for Streamlit
  # Flip the frame horizontally
  frame = cv2.flip(frame, 1)  # 1 for horizontal flip
  FRAME_WINDOW.image(frame)
  
  # Slow down frame update for better performance
  key = cv2.waitKey(1) & 0xFF
  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()
