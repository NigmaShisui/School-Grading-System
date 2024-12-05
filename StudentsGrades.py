import database

# Helper functions
def input_grade_component(component_name):
    """Helper function to input grades for a specific component."""
    while True:
        try:
            grade = float(input(f"Enter {component_name} grade (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def compute_final_grade(written_works, performance_tasks, quarterly_assessment):
    """Compute the final grade based on DepEd grading weights."""
    written_weight = 0.30
    performance_weight = 0.50
    quarterly_weight = 0.20

    final_grade = (
        (written_works * written_weight) +
        (performance_tasks * performance_weight) +
        (quarterly_assessment * quarterly_weight)
    )
    return round(final_grade, 2)

# Core functionalities
def input_student_grades(students=None):
    """Input grades for students."""
    if not students:
        print("No students found. Please add students first.")
        return

    print("\n=== Input Grades ===")
    for student in students:
        print(f"\nEntering grades for {student['name']} (Grade {student['grade_level']}):")
        grades = {}

        for subject in ["English", "Science", "Math"]:
            print(f"\n{subject}:")
            written = input_grade_component("Written Works")
            performance = input_grade_component("Performance Tasks")
            quarterly = input_grade_component("Quarterly Assessment")

            final_grade = compute_final_grade(written, performance, quarterly)
            grades[subject] = {
                "Written Works": written,
                "Performance Tasks": performance,
                "Quarterly Assessment": quarterly,
                "Final Grade": final_grade
            }

        student['grades'] = grades
    database.save_all("students", students)
    print("\nGrades successfully updated!")

def generate_reports(students=None):
    """Generate student grade reports including averages and rankings."""
    if not students:
        print("No students found. Please add students first.")
        return

    print("\n=== Generating Reports ===")
    rankings = []

    for student in students:
        grades = student.get('grades', {})
        total_grades = 0
        num_subjects = len(grades)

        print(f"\nReport for {student['name']} (Grade {student['grade_level']}):")
        print("Subject Grades:")

        for subject, details in grades.items():
            final_grade = details.get("Final Grade", 0)
            total_grades += final_grade
            print(f"  {subject}: {final_grade}%")

        average = round(total_grades / num_subjects, 2) if num_subjects > 0 else 0
        print(f"Average Grade: {average}%")

        if average >= 98:
            rank = "With Highest Honor"
        elif 95 <= average < 98:
            rank = "With High Honor"
        elif 90 <= average < 95:
            rank = "With Honor"
        elif average >= 75:
            rank = "Passed"
        else:
            rank = "Failed"

        print(f"Rank: {rank}")

        rankings.append({
            "name": student['name'],
            "average": average,
            "rank": rank
        })

    print("\n=== Rankings ===")
    rankings.sort(key=lambda x: x['average'], reverse=True)
    for idx, entry in enumerate(rankings, 1):
        print(f"{idx}. {entry['name']} - Average: {entry['average']}% - {entry['rank']}")

# Menus
def choose_students():
    """Allow the teacher to choose specific students or the entire list."""
    students = database.fetch_all("students")
    if not students:
        print("No students found. Please add students first.")
        return None

    print("\n1. Select a specific student")
    print("2. Proceed with the entire list")
    choice = input("Select an option: ").strip()

    if choice == '1':
        print("\nAvailable students:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student['name']} (Grade {student['grade_level']})")
        try:
            selected_index = int(input("Enter the number of the student: ")) - 1
            if 0 <= selected_index < len(students):
                return [students[selected_index]]
            else:
                print("Invalid selection.")
                return None
        except ValueError:
            print("Invalid input. Returning to the main menu.")
            return None
    elif choice == '2':
        return students
    else:
        print("Invalid choice. Returning to the main menu.")
        return None

def grading_menu():
    """Menu for grading system."""
    while True:
        print("================================================================")
        print("                 === Grading System ===")
        print("----------------------------------------------------------------")
        print("1. Input Grades for Students")
        print("2. Generate Student Reports and Rankings")
        print("3. Go Back")
        print("================================================================")

        choice = input("Select an option: ").strip()
        if choice == '1':
            selected_students = choose_students()
            if selected_students:
                input_student_grades(selected_students)
        elif choice == '2':
            selected_students = choose_students()
            if selected_students:
                generate_reports(selected_students)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
