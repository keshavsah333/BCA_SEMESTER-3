
import csv
import os

FILE = "students.csv"
FIELDS = ["RollNo", "Name", "Course", "Marks"]


def create_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)


def read_students():
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


def save_students(students):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    students = read_students()

    if any(s["RollNo"] == roll for s in students):
        print("Roll number already exists.")
        return

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll, name, course, marks])

    print("Student added successfully!")


def display_students():
    students = read_students()

    if not students:
        print("No student records found.")
        return

    print("\nAll Student Records:")
    for student in students:
        print(student)


def search_student():
    roll = input("Enter Roll No to search: ")

    for student in read_students():
        if student["RollNo"] == roll:
            print("Student found:", student)
            return

    print("Student not found.")


def update_student():
    roll = input("Enter Roll No to update: ")
    students = read_students()

    for student in students:
        if student["RollNo"] == roll:
            student["Name"] = input("Enter new Name: ")
            student["Course"] = input("Enter new Course: ")
            student["Marks"] = input("Enter new Marks: ")
            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    roll = input("Enter Roll No to delete: ")
    students = read_students()

    updated = [s for s in students if s["RollNo"] != roll]

    if len(updated) == len(students):
        print("Student not found.")
    else:
        save_students(updated)
        print("Student deleted successfully!")


def display_above_75():
    found = False

    print("\nStudents with marks above 75:")
    for student in read_students():
        if float(student["Marks"]) > 75:
            print(student)
            found = True

    if not found:
        print("No records found.")


def display_below_40():
    found = False

    print("\nStudents with marks below 40:")
    for student in read_students():
        if float(student["Marks"]) < 40:
            print(student)
            found = True

    if not found:
        print("No records found.")


def main():
    create_file()

    while True:
        print("\n========== STUDENT RECORD SYSTEM ==========")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Display Students Above 75 Marks")
        print("7. Display Students Below 40 Marks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            display_above_75()
        elif choice == "7":
            display_below_40()
        elif choice == "8":
            print("Exiting Student Record System.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()