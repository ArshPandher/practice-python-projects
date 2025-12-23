#Name - Arshpreet Singh
#Course - CS 11200
#Project title - Student Grade Manager

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):

        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def display_info(self):
        average = self.calculate_average()
        letter = self.get_letter_grade()

        print("\nStudent Report")
        print("--------------")
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter}\n")

def show_menu():
    print("\n1. Add a new student")
    print("2. Add grade to a student")
    print("3. View a student's report")
    print("4. View all students")
    print("5. Exit")


def add_new_student(students):
    name = input("Enter student name: ")
    s_id = input("Enter student ID: ")

    new_student = Student(name, s_id)
    students[s_id] = new_student

    print("Student added successfully!")


def add_grade_to_student(students):
    s_id = input("Enter student ID: ")

    if s_id in students:
        try:
            grade = float(input("Enter grade (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if 0 <= grade <= 100:
            students[s_id].add_grade(grade)
            print("Grade added!")
        else:
            print("Grade must be between 0 and 100.")
    else:
        print("Student not found.")


def view_student_report(students):
    s_id = input("Enter student ID: ")

    if s_id in students:
        students[s_id].display_info()
    else:
        print("Student not found.")


def view_all_students(students):
    if len(students) == 0:
        print("No students added yet.")
        return

    print("\nAll Students Summary")
    print("---------------------")
    for student in students.values():
        avg = student.calculate_average()
        print(f"Name: {student.name}, ID: {student.student_id}, Avg: {avg:.2f}")

def main():
    students = {}

    print("Welcome to the Student Grade Manager!")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_new_student(students)
        elif choice == "2":
            add_grade_to_student(students)
        elif choice == "3":
            view_student_report(students)
        elif choice == "4":
            view_all_students(students)
        elif choice == "5":
            print("Thank you for using the Student Grade Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
