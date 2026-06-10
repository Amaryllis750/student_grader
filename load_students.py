"""
load_students.py
----------------
Reads student data from a CSV file and returns it as a list of dicts.
This is the only pre-implemented module — do not modify it.

CSV format:
    name,math,english,science
    Alice Johnson,92,88,95
    ...
"""

import csv
from pathlib import Path


def load_students(filepath: str) -> list[dict]:
    """
    Load student records from a CSV file.
    Returns a list of dicts, e.g.:
        [{"name": "Alice", "math": 92.0, "english": 88.0, "science": 95.0}, ...]

    - Scores are returned as floats.
    - Rows with missing or invalid scores are skipped with a warning.
    - Raises FileNotFoundError if the file does not exist.
    """
    students = []
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {filepath}")

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=2):
            name = row.get("name", "").strip()
            if not name:
                print(f"  [warning] Row {i}: missing name, skipping.")
                continue

            scores = {}
            valid = True
            for subject in ("math", "english", "science"):
                raw = row.get(subject, "").strip()
                try:
                    score = float(raw)
                    if not (0 <= score <= 100):
                        raise ValueError("out of range")
                    scores[subject] = score
                except ValueError:
                    print(f"  [warning] Row {i} ({name}): invalid {subject} score '{raw}', skipping row.")
                    valid = False
                    break

            if valid:
                students.append({"name": name, **scores})

    return students
