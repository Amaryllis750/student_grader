"""
main.py — Student Grade Calculator
===================================
Entry point. Do not modify this file.

Run with:
    python main.py                    # uses data/students.csv
    python main.py data/my_class.csv  # custom CSV path
"""

import sys
from load_students import load_students
from grades import rank_students
from subjects import get_subject_stats, rank_by_subject


SUBJECTS = ("math", "english", "science")


def print_grade_report(ranked: list[dict]) -> None:
    print("\n" + "=" * 52)
    print(f"{'GRADE REPORT':^52}")
    print("=" * 52)
    print(f"{'Rank':<6}{'Name':<22}{'Average':>8}{'Grade':>6}")
    print("-" * 52)
    for i, s in enumerate(ranked, 1):
        print(f"{i:<6}{s['name']:<22}{s['average']:>8.2f}{s['grade']:>6}")
    print("=" * 52)


def print_subject_stats(stats: dict) -> None:
    print("\n" + "=" * 52)
    print(f"{'SUBJECT STATS':^52}")
    print("=" * 52)
    for subject, data in stats.items():
        print(f"\n  {subject.upper()}")
        print(f"    Best  : {data['best']['name']}  ({data['best']['score']})")
        print(f"    Worst : {data['worst']['name']}  ({data['worst']['score']})")
    print("\n" + "=" * 52)


def print_subject_ranking(students: list[dict], subject: str) -> None:
    print("\n" + "=" * 52)
    print(f"  RANKING BY {subject.upper()}")
    print("=" * 52)
    print(f"{'Rank':<6}{'Name':<30}{'Score':>8}")
    print("-" * 52)
    ranked = rank_by_subject(students, subject)
    for i, s in enumerate(ranked, 1):
        print(f"{i:<6}{s['name']:<30}{s[subject]:>8.2f}")
    print("=" * 52)


def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else "data/students.csv"

    print(f"\nLoading student data from: {filepath}")
    try:
        students = load_students(filepath)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not students:
        print("No valid student records found.")
        sys.exit(1)

    # ── Intern A ──────────────────────────────────────────
    ranked = rank_students(students)
    print_grade_report(ranked)

    # ── Intern B ──────────────────────────────────────────
    stats = get_subject_stats(students)
    print_subject_stats(stats)

    for subject in SUBJECTS:
        print_subject_ranking(students, subject)


if __name__ == "__main__":
    main()
