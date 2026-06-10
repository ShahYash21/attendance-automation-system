import pytesseract
import cv2
import re


# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_roll_numbers(image_path):
    """
    Extract roll numbers from processed attendance image.
    """

    # Read processed image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read processed image.")

    # Tesseract Configuration
    custom_config = r'--oem 3 --psm 6'

    # OCR Extraction
    extracted_text = pytesseract.image_to_string(
        image,
        config=custom_config
    )

    print("\n===== OCR OUTPUT =====")
    print(extracted_text)

    # Extract only numbers
    roll_numbers = re.findall(r'\d+', extracted_text)

    # Convert to integers
    roll_numbers = [int(num) for num in roll_numbers]

    # Remove duplicates
    roll_numbers = list(set(roll_numbers))

    # Sort roll numbers
    roll_numbers.sort()

    return roll_numbers