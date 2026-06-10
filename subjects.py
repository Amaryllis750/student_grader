"""
subjects.py  —  Intern B
------------------------
Implement the two functions below.
Use load_students() from load_students.py to get your input data.

Subjects available: math, english, science
"""


def get_subject_stats(students: list[dict]) -> dict:
    """
    For each subject, find the student with the highest and lowest score.
    Returns a dict keyed by subject name, each containing 'best' and 'worst'.

    Example:
        {
            "math":    {"best": {"name": "Emma", "score": 98}, "worst": {"name": "Henry", "score": 45}},
            "english": {"best": {"name": "Emma", "score": 95}, "worst": {"name": "Henry", "score": 50}},
            "science": {"best": {"name": "Emma", "score": 99}, "worst": {"name": "Henry", "score": 48}},
        }
    """
    pass


def rank_by_subject(students: list[dict], subject: str) -> list[dict]:
    """
    Return the list of students sorted by a given subject score, descending.
    Raise a ValueError if the subject is not one of: math, english, science.

    Example:
        rank_by_subject(students, "math")
        → students sorted from highest to lowest math score
    """
    pass
