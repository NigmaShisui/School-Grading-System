import database

def generate_reports():
    #to generate a detailed report for each student
    students = database.fetch_all("students")
    if not students:
        print("No students found.")
        return

    print("\n=== Student Reports ===")
    ranked_students = []

    for student in students:
        total_average = 0
        print(f"\nReport for {student['name']} (Grade {student['grade_level']}):")
        for subject, grade in student['grades'].items():
            print(f"{subject}: {grade:.2f}")
            total_average += grade
        average = total_average / len(student['grades'])
        print(f"Average: {average:.2f}")
        student['average'] = average

        # for determining the passing/failing status
        if average < 75:
            student['status'] = "Failed"
            student['honor'] = None
        elif average < 90:
            student['status'] = "Passed"
            student['honor'] = None
        else:
            student['status'] = "Passed"
            # for determining the honors
            if average >= 98:
                student['honor'] = "With Highest Honors"
            elif average >= 95:
                student['honor'] = "With High Honors"
            elif average >= 90:
                student['honor'] = "With Honors"

        print(f"Status: {student['status']}")
        if student['honor']:
            print(f"Honor: {student['honor']}")

        if student['honor']:
            ranked_students.append(student)

    # Save updated averages, status, and honors
    database.save_all("students", students)

    # Sort and display ranked students
    if ranked_students:
        print("\n=== Ranked Students ===")
        ranked_students.sort(key=lambda x: x['average'], reverse=True)
        for idx, student in enumerate(ranked_students, 1):
            print(f"{idx}. {student['name']} - {student['honor']} ({student['average']:.2f})")


def view_ranked_students():
    #Displays all students with honors and sorted by ranks
    students = database.fetch_all("students")
    if not students:
        print("No students found.")
        return

    ranked_students = [s for s in students if s.get('honor')]
    if not ranked_students:
        print("No ranked students found.")
        return

    print("\n=== Ranked Students ===")
    ranked_students.sort(key=lambda x: x['average'], reverse=True)
    for idx, student in enumerate(ranked_students, 1):
        print(f"{idx}. {student['name']} - {student['honor']} ({student['average']:.2f})")


def reports_menu():
    """Menu for grading system."""
    while True:
        print("============================")
        print("  === Report Generator ===")
        print("----------------------------")
        print(" ")
        print("    1. Generate Reports")
        print("    2. Students Ranking")
        print("    3. Go Back")
        print(" ")
        print("============================")

        choice = int(input("Select an option: ")).strip()
        if choice == 1:
            generate_reports()
        elif choice == 2:
            view_ranked_students()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")