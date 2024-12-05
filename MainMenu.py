from StudentsGrades import grading_menu
from ManageStudent import manage_students_menu

def main_menu():
    """Main menu for the School Grading System."""
    while True:
        print("================================================================")
        print("                  === School Grading System ===")
        print("----------------------------------------------------------------")
        print("1. Manage Students")
        print("2. Grading System and Reports")
        print("3. Exit")
        print("================================================================")

        # Input validation
        try:
            choice = int(input("Select an option: ").strip())
            if choice == 1:
                manage_students_menu()
            elif choice == 2:
                grading_menu()
            elif choice == 3:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Run the main menu
main_menu()
