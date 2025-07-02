# Student Grading System
# Stores student data in a list of dictionaries and calculates average and grade

def calculate_average(marks):
    return sum(marks) / len(marks)

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    else:
        return 'C'

def find_highest_subject(subjects, marks):
    highest_mark = max(marks)
    highest_index = marks.index(highest_mark)
    return subjects[highest_index]

def main():
    students = []
    subjects = ["Math", "Science", "English"]
    
    while True:
        print("\nStudent Grading System")
        name = input("Enter student name (or 'quit' to exit): ")
        
        if name.lower() == 'quit':
            break
            
        marks = []
        for subject in subjects:
            while True:
                try:
                    mark = float(input(f"Enter {subject} mark (0-100): "))
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Mark must be between 0 and 100")
                except ValueError:
                    print("Please enter a valid number")
        
        average = calculate_average(marks)
        grade = determine_grade(average)
        highest_subject = find_highest_subject(subjects, marks)
        
        student = {
            'name': name,
            'marks': marks,
            'average': average,
            'grade': grade,
            'highest_subject': highest_subject
        }
        students.append(student)
        
        print(f"\nResults for {name}:")
        print(f"Average: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Highest Subject: {highest_subject} ({max(marks)})")

    # Print summary of all students
    if students:
        print("\nSummary of all students:")
        for student in students:
            print(f"\nName: {student['name']}")
            print(f"Average: {student['average']:.2f}")
            print(f"Grade: {student['grade']}")
            print(f"Highest Subject: {student['highest_subject']}")

if __name__ == "__main__":
    main()
