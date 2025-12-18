import matplotlib.pyplot as plt
import pandas as pd
import os
from student_grader.core_logic.score_statistics import StudentStatistics, CohortStatistics

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
STUDENT_PATH = os.path.join(FOLDER_PATH, "..", "..", "student_grader", "data", "students.csv") 

def is_student_valid(student_id):
    df = pd.read_csv(STUDENT_PATH, index_col="student_id")
    return student_id in df.index

def analyse_student(*, student_id):
    if not is_student_valid(student_id):
        print("Please enter a valid student from the database.")
        return
     
    non_exam_score = StudentStatistics.non_exam_score(student_id) * 0.6
    exam_score = StudentStatistics.exam_score(student_id) * 0.4

    labels = ["Exam Score", "Coursework Score"]
    scores = [exam_score, non_exam_score]

    plt.pie(
        scores,
        labels=labels,
        autopct='%1.1f%%'
    )

    plt.title("Student Analyse")
    plt.axis('equal')
    plt.show()