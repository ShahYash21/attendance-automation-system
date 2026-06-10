import pandas as pd


def mark_attendance(students_file, present_rolls):
    """
    Marks attendance based on OCR-detected roll numbers.
    """

    # Read student database
    df = pd.read_excel(students_file)

    # Total students in database
    total_students = len(df)

    valid_rolls = []
    invalid_rolls = []

    # Validate roll numbers
    for roll in present_rolls:
        if 1 <= roll <= total_students:
            valid_rolls.append(roll)
        else:
            invalid_rolls.append(roll)

    # Remove duplicates
    valid_rolls = list(set(valid_rolls))

    # Show warnings
    if invalid_rolls:
        print("\n===== WARNING =====")
        print("Invalid roll numbers ignored:")
        print(invalid_rolls)

    # Mark attendance
    df["Status"] = df["Roll No"].apply(
        lambda roll: "P" if roll in valid_rolls else "A"
    )

    return df