class Student:
    def __init__(self, name, age, grades):
        """Constructor to initialize name, age, and grades."""
        self.name = name
        self.age = age
        self.grades = grades  

    def display_details(self):
        """Method to display the details of the student."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {', '.join(map(str, self.grades))}")

    def calculate_average_grade(self):
        """Method to calculate the average grade."""
        if self.grades:  
            return sum(self.grades) / len(self.grades)
        return 0  
def main():
    student_name = input("Enter student's name: ")
    student_age = int(input("Enter student's age: "))
    student_grades = input("Enter student's grades (comma separated): ").split(',')
    student_grades = [float(grade.strip()) for grade in student_grades]  # Convert grades to float

    student = Student(student_name, student_age, student_grades)
    print("\nStudent Details:")
    student.display_details()
    avg_grade = student.calculate_average_grade()
    print(f"Average Grade: {avg_grade:.2f}")

if __name__ == "__main__":
    main()
