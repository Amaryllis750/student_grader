# 📊 Student Grade Calculator

A command-line tool that reads student scores and produces grade and subject reports.

**One function is already implemented** (`load_students`). Your job is to implement the rest.

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/your-org/grade-calculator.git
cd grade-calculator

# 2. Install dev dependencies
pip install pytest

# 3. Run the tests (all will fail at first — that's expected)
python -m pytest tests/ -v

# 4. Once implemented, run the program
python main.py
```

---

## Project Structure

```
grade-calculator/
├── main.py             ✅ Already implemented — do not modify
├── load_students.py    ✅ Already implemented — do not modify
├── grades.py           ⬜ Intern A
├── subjects.py         ⬜ Intern B
├── data/
│   └── students.csv
└── tests/
    └── test_all.py
```

---

## Tasks

### Intern A — `grades.py`
- `compute_average(student)` — mean of math, english, science
- `assign_letter_grade(average)` — maps a number to A/B/C/D/F
- `rank_students(students)` — adds average + grade to each student, sorts descending

### Intern B — `subjects.py`
- `get_subject_stats(students)` — best and worst student per subject
- `rank_by_subject(students, subject)` — sorts students by a given subject score

---

## Grading Scale

| Average | Grade |
|---------|-------|
| 90–100  | A     |
| 80–89   | B     |
| 70–79   | C     |
| 60–69   | D     |
| 0–59    | F     |

---

## Expected Output

```
====================================================
                    GRADE REPORT
====================================================
Rank  Name                  Average  Grade
----------------------------------------------------
1     Emma Brown              97.33      A
2     Alice Johnson           91.67      A
3     Carol White             87.67      B
...

====================================================
                   SUBJECT STATS
====================================================

  MATH
    Best  : Emma Brown  (98.0)
    Worst : Henry Wilson  (45.0)

  ENGLISH
    Best  : Emma Brown  (95.0)
    Worst : Henry Wilson  (50.0)
...

====================================================
  RANKING BY MATH
====================================================
Rank  Name                          Score
----------------------------------------------------
1     Emma Brown                    98.00
2     Alice Johnson                 92.00
...
```

---

## Git Workflow

```
main (protected)  ← PRs only
  └── develop
        └── feature/<your-name>-<module>
```

1. Pull latest `develop`
2. Create your branch: `feature/alice-grades` or `feature/bob-subjects`
3. Implement your functions
4. Make sure your tests pass: `python -m pytest tests/ -v`
5. Push and open a PR to `develop`
