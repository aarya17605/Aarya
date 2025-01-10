students = {}
def create_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = input("Enter student's grades (comma separated): ").split(',')
    grades = [grade.strip() for grade in grades]  # Clean up extra spaces
    students[name] = {'age': age, 'grades': grades}
    print(f"Student {name} added successfully!")

def read_student():
    name = input("Enter student's name to search: ")
    if name in students:
        student = students[name]
        print(f"Name: {name}, Age: {student['age']}, Grades: {', '.join(student['grades'])}")
    else:
        print(f"Student {name} not found.")

def update_student():
    name = input("Enter student's name to update: ")
    if name in students:
        age = int(input(f"Enter new age for {name}: "))
        grades = input(f"Enter new grades for {name} (comma separated): ").split(',')
        grades = [grade.strip() for grade in grades]
        students[name] = {'age': age, 'grades': grades}
        print(f"Student {name} updated successfully!")
    else:
        print(f"Student {name} not found.")

def delete_student():
    name = input("Enter student's name to delete: ")
    if name in students:
        del students[name]
        print(f"Student {name} deleted successfully!")
    else:
        print(f"Student {name} not found.")

def display_all_students():
    if students:
        print("\nAll Student Records:")
        for name, data in students.items():
            print(f"Name: {name}, Age: {data['age']}, Grades: {', '.join(data['grades'])}")
    else:
        print("No student records found.")

def main():
    while True:
        print("\nStudent Data Management System")
        print("1. Add New Student")
        print("2. View Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            read_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_all_students()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
