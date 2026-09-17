students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


def display_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print("--------------------")
        print("Name:", student["name"])
        print("Roll No:", student["roll_no"])
        print("Marks:", student["marks"])


def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
