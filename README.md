# week1-task--Anuj-baghel-
# Week 1 Task: Student Grading System

## Approach
This program implements a student grading system in Python that:
1. Takes input for student names and marks for three subjects (Math, Science, English)
2. Calculates the average mark
3. Determines a grade (A/B/C) based on the average
4. Identifies the highest-scoring subject
5. Stores all student data in a list of dictionaries
6. Provides a summary of all students' results

## Assumptions
- Marks are valid numbers between 0 and 100
- Grading scale:
  - A: 90-100
  - B: 80-89
  - C: Below 80
- Program continues accepting student data until user enters 'quit'
- Input validation ensures marks are valid numbers within range
- Subjects are fixed as Math, Science, and English

## Results
The program:
- Prompts for student name and marks
- Validates input to ensure proper number format and range
- Calculates and displays:
  - Average mark (rounded to 2 decimal places)
  - Letter grade (A/B/C)
  - Highest scoring subject with its mark
- Stores all data in a list of dictionaries
- Displays a summary of all students when program ends
- Handles invalid inputs gracefully with error messages

## How to Run
1. Save the code as `student_grading_system.py`
2. Run using Python 3: `python student_grading_system.py`
3. Follow prompts to enter student data
4. Enter 'quit' to see summary and exit

## Repository Structure
- `student_grading_system.py`: Main Python program
- `README.md`: This documentation file
