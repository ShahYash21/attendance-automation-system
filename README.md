# Attendance Automation System

## Overview

The Attendance Automation System is a Python-based application that automates the process of marking student attendance from structured attendance images. The system extracts roll numbers using Optical Character Recognition (OCR) techniques and generates an Excel attendance report automatically.

This project was developed to reduce manual effort involved in transferring attendance records into spreadsheets.

---

## Features

* Extracts roll numbers from structured attendance images.
* Performs image preprocessing to improve OCR accuracy.
* Handles duplicate roll numbers automatically.
* Validates extracted roll numbers against the student database.
* Ignores invalid roll numbers and displays warning messages.
* Generates attendance reports in Excel format.
* Reduces manual attendance processing effort.

---

## Technologies Used

* **Python**
* **OpenCV** – Image preprocessing
* **Tesseract OCR** – Text extraction from images
* **Pandas** – Data manipulation
* **OpenPyXL** – Excel file generation

---

## Project Structure

```text
Attendance_Automation_System/
│
├── main.py
├── requirements.txt
├── README.md
│
├── data/
│   └── students.xlsx
│
├── input/
│   └── attendance_photo.jpg
│
├── output/
│   ├── processed_image.jpg
│   └── attendance_result.xlsx
│
├── modules/
│   ├── image_processor.py
│   ├── ocr_reader.py
│   ├── attendance_marker.py
│   └── excel_writer.py
│
└── .gitignore
```

## Workflow

```text
Attendance Image
        ↓
Image Preprocessing (OpenCV)
        ↓
Text Extraction (Tesseract OCR)
        ↓
Roll Number Validation
        ↓
Attendance Marking
        ↓
Excel Report Generation
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/ShahYash21/attendance-automation-system.git
cd attendance-automation-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Tesseract OCR

Download and install Tesseract OCR from:

https://github.com/UB-Mannheim/tesseract/wiki

Update the Tesseract path in the project if required.

---

## Usage

1. Add the student database Excel file to the `data` folder.
2. Place the attendance image inside the `input` folder.
3. Run the application:

```bash
python main.py
```

4. The generated attendance report will be available in the `output` folder.

---

## Sample Output

The generated Excel report contains:

| Roll No | Name     | Status |
| ------- | -------- | ------ |
| 1       | Student1 | P      |
| 2       | Student2 | A      |
| 3       | Student3 | P      |

---

## Limitations

* The current implementation works best with structured attendance images having clear and high-contrast digits.
* Complex handwritten patterns and low-quality images may affect OCR accuracy.

---

## Future Enhancements

* Support for handwritten attendance sheets using deep learning techniques.
* User-friendly graphical interface.
* Cloud-based attendance storage and analytics.
* Real-time attendance processing.

---

## Author

**Yash Shah**

GitHub: https://github.com/ShahYash21

LinkedIn: Add your LinkedIn profile link here.
