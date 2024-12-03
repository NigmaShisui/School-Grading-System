import database

#for subject grades
def subject_grades():
    #Allows the teacher to input grades for all subjects
    students = database.fetch_all("students")
    if not students:
        print("No students found. Please add students first.")
        return

    print("\n=== Input Grades ===")
    for student in students:
        print(f"\nEntering grades for {student['name']} (Grade {student['grade_level']}):")
        student['grades'] = {
            "Math": input_grade("Math"),
            "Science": input_grade("Science"),
            "English": input_grade("English"),
            "Filipino": input_grade("Filipino"),
            "Physical Education": input_grade("Physical Education"),
            "Araling Panlipunan": input_grade("Araling Panlipunan"),
            "ICT": input_grade("ICT"),
            "TLE": input_grade("TLE"),
            "ESP": input_grade("ESP"),
        }
    database.save_all("students", students)
    print("\nGrades successfully updated!")

#for attendance, written works, and for performance task
def input_grade(subject):
    #Helper function to input points for AWP Task
    print(f"\n{subject}:")
    attendance = int(input("Enter Attendance Points: "))
    written_work = int(input("Enter Written Points: "))
    performance_task = int(input("Enter Performance Task Points: "))
    exam = int(input("Enter Exam Points: "))

    total = attendance + written_work + performance_task + exam
    return total / 4


def grading_menu():
    """Menu for grading system."""
    while True:
        print("================================================================")
        print("                 === Grading System ===")
        print("----------------------------------------------------------------")
        print(" ")
        print("            1. Students Grades per Subjects")
        print("  2. Students Attendance, Written, and Performance Task Points")
        print("                      3. Go Back")
        print(" ")
        print("================================================================")

        choice = input("Select an option: ").strip()
        if choice == '1':
            subject_grades()
        elif choice == '2':
            input_grade()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")