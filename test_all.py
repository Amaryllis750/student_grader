"""
tests/test_grades.py & test_subjects.py combined
-------------------------------------------------
All tests will FAIL until you implement your functions.
Run with: python -m pytest tests/ -v
"""

import pytest
from grades import compute_average, assign_letter_grade, rank_students
from subjects import get_subject_stats, rank_by_subject


SAMPLE_STUDENTS = [
    {"name": "Alice", "math": 90.0, "english": 80.0, "science": 70.0},
    {"name": "Bob",   "math": 50.0, "english": 60.0, "science": 55.0},
    {"name": "Carol", "math": 75.0, "english": 85.0, "science": 95.0},
]


# ── Intern A: grades.py ───────────────────────────────────────────────────────

class TestComputeAverage:
    def test_equal_scores(self):
        s = {"name": "X", "math": 80, "english": 80, "science": 80}
        assert compute_average(s) == 80.0

    def test_mixed_scores(self):
        s = {"name": "X", "math": 90, "english": 70, "science": 80}
        assert compute_average(s) == 80.0

    def test_perfect_scores(self):
        s = {"name": "X", "math": 100, "english": 100, "science": 100}
        assert compute_average(s) == 100.0

    def test_zero_scores(self):
        s = {"name": "X", "math": 0, "english": 0, "science": 0}
        assert compute_average(s) == 0.0


class TestAssignLetterGrade:
    @pytest.mark.parametrize("avg,expected", [
        (95, "A"), (90, "A"),
        (89, "B"), (80, "B"),
        (79, "C"), (70, "C"),
        (69, "D"), (60, "D"),
        (59, "F"), (0,  "F"),
    ])
    def test_grade_boundaries(self, avg, expected):
        assert assign_letter_grade(avg) == expected


class TestRankStudents:
    def test_sorted_descending(self):
        ranked = rank_students(SAMPLE_STUDENTS)
        averages = [s["average"] for s in ranked]
        assert averages == sorted(averages, reverse=True)

    def test_has_average_and_grade(self):
        ranked = rank_students(SAMPLE_STUDENTS)
        for s in ranked:
            assert "average" in s
            assert "grade" in s

    def test_correct_grade_assigned(self):
        ranked = rank_students(SAMPLE_STUDENTS)
        alice = next(s for s in ranked if s["name"] == "Alice")
        assert alice["average"] == 80.0
        assert alice["grade"] == "B"

    def test_empty_list(self):
        assert rank_students([]) == []


# ── Intern B: subjects.py ─────────────────────────────────────────────────────

class TestGetSubjectStats:
    def test_returns_all_subjects(self):
        stats = get_subject_stats(SAMPLE_STUDENTS)
        assert "math" in stats
        assert "english" in stats
        assert "science" in stats

    def test_best_and_worst_keys(self):
        stats = get_subject_stats(SAMPLE_STUDENTS)
        for subject in ("math", "english", "science"):
            assert "best" in stats[subject]
            assert "worst" in stats[subject]

    def test_correct_best_math(self):
        stats = get_subject_stats(SAMPLE_STUDENTS)
        assert stats["math"]["best"]["name"] == "Alice"
        assert stats["math"]["best"]["score"] == 90.0

    def test_correct_worst_math(self):
        stats = get_subject_stats(SAMPLE_STUDENTS)
        assert stats["math"]["worst"]["name"] == "Bob"
        assert stats["math"]["worst"]["score"] == 50.0

    def test_correct_best_science(self):
        stats = get_subject_stats(SAMPLE_STUDENTS)
        assert stats["science"]["best"]["name"] == "Carol"
        assert stats["science"]["best"]["score"] == 95.0


class TestRankBySubject:
    def test_sorted_by_math_descending(self):
        ranked = rank_by_subject(SAMPLE_STUDENTS, "math")
        scores = [s["math"] for s in ranked]
        assert scores == sorted(scores, reverse=True)

    def test_sorted_by_english_descending(self):
        ranked = rank_by_subject(SAMPLE_STUDENTS, "english")
        scores = [s["english"] for s in ranked]
        assert scores == sorted(scores, reverse=True)

    def test_invalid_subject_raises(self):
        with pytest.raises(ValueError):
            rank_by_subject(SAMPLE_STUDENTS, "history")

    def test_returns_all_students(self):
        ranked = rank_by_subject(SAMPLE_STUDENTS, "science")
        assert len(ranked) == len(SAMPLE_STUDENTS)
