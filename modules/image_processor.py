import cv2
import os
import numpy as np


def preprocess_image(image_path):
    """
    Reads the attendance image and prepares it for OCR.
    """

    # Check if image exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read the image.")

    # Resize image (helps OCR accuracy)
    image = cv2.resize(image, None, fx=2, fy=2)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive Thresholding
    thresh = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # Morphological Opening (removes small noise)
    kernel = np.ones((2, 2), np.uint8)
    thresh = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel
    )

    # Save processed image
    processed_path = "output/processed_image.jpg"

    cv2.imwrite(processed_path, thresh)

    return processed_path