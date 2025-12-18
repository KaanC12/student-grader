import matplotlib.pyplot as plt
import pandas as pd
import os
from student_grader.core_logic.score_statistics import StudentStatistics, CohortStatistics
from student_grader.services.student_service import *
from student_grader.exceptions.exceptions import InvalidStudent

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
STUDENT_PATH = os.path.join(FOLDER_PATH, "..", "..", "student_grader", "data", "students.csv") 

STUDENT_IS_INVALID = "Please enter a valid student from the database."
STUDENT_VALUES_INVALID = "Pleas generate a valid student."

def is_student_valid(student_id):
    df = pd.read_csv(STUDENT_PATH, index_col="student_id")
    return student_id in df.index

def set_student(*, student: dict):
    if len(student) != 3:
        raise ValueError(STUDENT_VALUES_INVALID)
    
    student_id = student[0]
    non_exam_score = student[1]
    exam_score = student[2] 

    add_student(student_id, non_exam_score, exam_score)

def remove_student(*, student_id):
    delete_student(student_id)

def change_exam_grade(*, student_id, new_grade):
    change_exam_score(student_id, new_grade)

def change_coursework_grade(*, student_id, new_grade):
    change_non_exam_score(student_id, new_grade)

def add_students(*, file_path):
    import_students_from_excel(file_path)

def analyse_student(*, student_id):
    if not is_student_valid(student_id):
        raise InvalidStudent(STUDENT_IS_INVALID)
    
    stats = StudentStatistics()

    non_exam_score = stats.non_exam_score(student_id) * 0.6
    exam_score = stats.exam_score(student_id) * 0.4

    labels = ["Exam Score", "Coursework Score"]
    scores = [exam_score, non_exam_score]

    delta = abs(stats.score_delta(student_id))
    average_score = stats.average_score(student_id)

    labels_bar = ["Difference between exams", "Average Score"]
    inputs = [delta, average_score]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].pie(
        scores,
        labels=labels,
        autopct='%1.1f%%'
    )
    axes[0].set_title("Score Distribution")
    axes[0].axis('equal')

    axes[1].bar(labels_bar, inputs)
    axes[1].set_title("Score Comparison")

    fig.suptitle(f"Student Analysis for {student_id}")
    
    plt.tight_layout()
    plt.show()

def show_grades(*, student_id):
    if not is_student_valid(student_id):
        raise InvalidStudent(STUDENT_IS_INVALID)
    
    stats = StudentStatistics()

    non_exam_score = stats.non_exam_score(student_id)
    exam_score = stats.exam_score(student_id)
    final_score = stats.final_score(student_id)

    labels = ["Exam Score", "Coursework Score"]
    scores = [exam_score, non_exam_score]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    bars = axes[0].bar(labels, scores)
    axes[0].set_title("Lecture Grades")

    for bar in bars:
        height = bar.get_height()
        axes[0].text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height: .1f}",
            ha="center",
            va="bottom"
        )
    
    passed = stats.is_passing(student_id)

    color = "green" if passed else "red"

    axes[1].barh(["Final Score"], [final_score], color=color)
    axes[1].axvline(40, color="black", linestyle="--", label="Pass limit")
    axes[1].set_xlim(0, 100)
    axes[1].legend()

    fig.suptitle("Student Grades.")

    plt.tight_layout()
    plt.show()

def average_class_grades():
    stats = CohortStatistics()

    average_exam_score = stats.exam_average()
    average_non_exam_score = stats.coursework_average()

    labels = ["Average Exam Grade", "Average Coursework Grade"]
    scores = [average_exam_score, average_non_exam_score]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    axes[0].bar(labels, scores)
    axes[0].set_title("Average Grades")

    successful_students = len(stats.has_passed())
    failed_students = len(stats.has_failed())

    labels_student_situation = ["Successful Students", "Failed Students"]
    values = [successful_students, failed_students]

    axes[1].bar(labels_student_situation, values)
    axes[1].set_title("Who is successful?")

    plt.tight_layout()
    plt.show()

def student_grades():
    stats = CohortStatistics()
    student_stat = StudentStatistics()

    passed_students = stats.has_passed()
    failed_students = stats.has_failed()

    passed_notes = []
    for student in passed_students:
        passed_notes.append(student_stat.final_score(student))

    failed_notes = []
    for student in failed_students:
        failed_notes.append(student_stat.final_score(student))

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].plot(
        passed_students, passed_notes,
        color="green",
        marker="o",
        linewidth=2,
        linestyle="--",
        label="Passed Students"
    )

    axes[0].plot(
        failed_students, failed_notes,
        color="red",
        marker="o",
        linewidth=2,
        linestyle="--",
        label="Failed Students"
    )

    axes[0].set_title("Student Scores")
    axes[0].set_xlabel("Students")
    axes[0].set_ylabel("Notes")
    axes[0].legend()

    axes[1].bar(
        ["Passed", "Failed"],
        [len(passed_students), len(failed_students)],
        color=["green", "red"]
    )

    axes[1].set_title("Pass / Fail Count")
    axes[1].set_ylabel("Number of Students")

    plt.tight_layout()
    plt.show()
    
