# Student Marks and Grade Calculator
# Syllabus: variables, input/output, type conversion, arithmetic,
# relational operators, and if-elif-else.

number_of_subjects = int(input("Enter number of subjects: "))

if number_of_subjects <= 0:
    print("Number of subjects must be positive.")
else:
    total = 0
    valid = True

    for subject in range(1, number_of_subjects + 1):
        marks = float(input(f"Enter marks for subject {subject} (0-100): "))

        if marks < 0 or marks > 100:
            print("Invalid marks. Enter marks between 0 and 100.")
            valid = False
            break

        total += marks

    if valid:
        average = total / number_of_subjects

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        elif average >= 40:
            grade = "E"
        else:
            grade = "F"

        print("\n----- Student Result -----")
        print(f"Total Marks: {total:g}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
