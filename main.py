from modules.image_processor import preprocess_image
from modules.ocr_reader import extract_roll_numbers
from modules.attendance_marker import mark_attendance
from modules.excel_writer import save_attendance


def main():
    print("\n===== Attendance Automation System =====")

    image_path = "input/attendance_photo.jpg"
    students_file = "data/students.xlsx"
    output_file = "output/attendance_result.xlsx"

    print("\nStep 1: Processing image...")
    processed_image = preprocess_image(image_path)

    print("Image processed successfully!")

    print("\nStep 2: Extracting roll numbers...")
    present_rolls = extract_roll_numbers(processed_image)

    print("Present Roll Numbers:", present_rolls)

    print("\nStep 3: Marking attendance...")
    attendance_df = mark_attendance(students_file, present_rolls)

    print("Attendance marked successfully!")

    print("\nStep 4: Generating Excel file...")
    save_attendance(attendance_df, output_file)

    print("\nAttendance sheet generated successfully!")
    print(f"Output File: {output_file}")


if __name__ == "__main__":
    main()