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


def compute_average(student: dict) -> float:
    """
    Return the mean score across math, english, and science for one student.

    Example:
        student = {"name": "Alice", "math": 90, "english": 80, "science": 70}
        compute_average(student) → 80.0
    """
    pass


def assign_letter_grade(average: float) -> str:
    """
    Map a numeric average to a letter grade using the grading scale above.

    Example:
        assign_letter_grade(85.0) → "B"
        assign_letter_grade(59.9) → "F"
    """
    pass


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
    pass
