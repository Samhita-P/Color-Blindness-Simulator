import cv2
import numpy as np
import streamlit as st
from PIL import Image, ExifTags

# Function to correct image orientation using EXIF metadata
def correct_orientation(image):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break

        exif = image._getexif()
        if exif is not None and orientation in exif:
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass  # Image has no EXIF data

    return image

# Color Blindness Simulation Matrices
color_blindness_matrices = {
    "Protanopia (Red-Blind)": np.array([[0.567, 0.433, 0],
                                        [0.558, 0.442, 0],
                                        [0, 0.242, 0.758]]),

    "Deuteranopia (Green-Blind)": np.array([[0.625, 0.375, 0],
                                            [0.7, 0.3, 0],
                                            [0, 0.3, 0.7]]),

    "Tritanopia (Blue-Blind)": np.array([[0.95, 0.05, 0],
                                         [0, 0.433, 0.567],
                                         [0, 0.475, 0.525]])
}

# Function to simulate color blindness
def simulate_color_blindness(image, matrix):
    img_float = np.array(image).astype(float) / 255.0
    simulated = np.dot(img_float, matrix.T)
    simulated = np.clip(simulated, 0, 1)
    return (simulated * 255).astype(np.uint8)

# Function to apply Daltonization correction
def apply_correction(simulated, matrix):
    correction_matrix = np.linalg.pinv(matrix)  # Compute pseudo-inverse
    corrected = np.dot(simulated.astype(float) / 255.0, correction_matrix.T)
    corrected = np.clip(corrected, 0, 1)
    return (corrected * 255).astype(np.uint8)

# Streamlit UI
st.set_page_config(page_title="Color Blindness Simulator", layout="wide")

st.title("🎨 Color Blindness Simulator & Correction")
st.write("Upload an image to simulate different types of color blindness and see the corrected version.")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded image to OpenCV format
    image = Image.open(uploaded_file)
    image = correct_orientation(image)  # Fix EXIF rotation issues
    image_np = np.array(image)

    # Ensure horizontal layout
    img_width, img_height = image.size
    if img_width > img_height:
        display_width = 500  # Wider display for horizontal images
    else:
        display_width = 350  # Smaller display for vertical images

    # Display Original Image
    st.image(image_np, caption="Original Image", width=display_width)

    # Select Color Blindness Type
    blindness_type = st.selectbox("Select Color Blindness Type", list(color_blindness_matrices.keys()))

    if st.button("Apply Simulation & Correction"):
        matrix = color_blindness_matrices[blindness_type]
        simulated_image = simulate_color_blindness(image_np, matrix)
        corrected_image = apply_correction(simulated_image, matrix)

        # Display Images Side-by-Side (Ensuring Horizontal Layout)
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(simulated_image, caption=f"{blindness_type} (Simulated)", width=display_width)

        with col2:
            st.image(corrected_image, caption=f"{blindness_type} (Original)", width=display_width)
