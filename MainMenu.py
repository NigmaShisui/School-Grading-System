from ManageStudent import manage_students_menu
from StudentsGrades import grading_menu
from StudentsReports import reports_menu
import database

def main_menu():
    """Main menu to navigate between features."""
    while True:
        print("====================================")
        print("  === School Management System ===")
        print("====================================")
        print(" ")
        print("         1. Manage Students")
        print("         2. Manage Grades")
        print("         3. View Reports")
        print("         4. Exit")
        print(" ")
        print("====================================")

        choice = input("Select an option: ").strip()
        if choice == '1':
            manage_students_menu()
        elif choice == '2':
            grading_menu()
        elif choice == '3':
            reports_menu()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
