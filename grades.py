"""
grades.py  —  Intern A
----------------------
Implement the three functions below.
Use load_students() from load_students.py to get your input data.

Grading scale:
    90 - 100  →  A
    80 -  89  →  B
    70 -  79  →  C
    60 -  69  →  D
     0 -  59  →  F
"""

student = {"name": "Alice", "math": 90, "english": 80, "science": 70}
def compute_average(student: dict) -> float:
    
    return (
    student["math"] + student["english"] + student["science"]) /3
    pass


def assign_letter_grade(average: float) -> str:
    """
    Map a numeric average to a letter grade using the grading scale above.

    Example:
        assign_letter_grade(85.0) → "B"
        assign_letter_grade(59.9) → "F"
    """
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


def rank_students(students: list[dict]) -> list[dict]:
    """
    Given a list of student dicts, return a new list where each student
    has two extra fields: 'average' (float, 2 dp) and 'grade' (str),
    sorted by average descending.

    Tip: use compute_average() and assign_letter_grade() inside here.

    Example:
        Input:  [{"name": "Bob", "math": 60, ...}, {"name": "Alice", "math": 90, ...}]
        Output: [{"name": "Alice", ..., "average": 90.0, "grade": "A"},
                 {"name": "Bob",   ..., "average": 60.0, "grade": "D"}]
    """
    ranked_students = []

    for student in students:
        average = compute_average(student)

        updated_student = student.copy()
        updated_student["average"] = average
        updated_student["grade"] = assign_letter_grade(average)

        ranked_students.append(updated_student)

    ranked_students.sort(
        key=lambda student: student["average"],
        reverse=True
    )

    return ranked_students
    
