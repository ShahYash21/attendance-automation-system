def save_attendance(attendance_df, output_file):
    """
    Saves attendance DataFrame to an Excel file.
    """

    attendance_df.to_excel(output_file, index=False)

    print(f"Attendance saved successfully to {output_file}")