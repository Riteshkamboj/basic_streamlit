import streamlit as st

def main():
    st.title("Webcam Feed")

    # Get the webcam input
    webcam_input = st.camera_input("Capture your webcam feed")

    if webcam_input is not None:
        # Display the webcam feed
        st.image(webcam_input, use_column_width=True)

if __name__ == "__main__":
    main()
