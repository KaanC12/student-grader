import os
import pandas as pd
from student_grader.exceptions import StudentAlreadyExistsError, EmptyDatabaseError

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_DIR = CURRENT_DIR[:len(CURRENT_DIR) - 1 - len("services")]
TARGET_DIR = os.path.join(FOLDER_DIR, "data", "students.csv")


def is_file_empty(path):
    if os.path.getsize(path) > 0:
        return True
    else:
        return False

def add_student(*, student_id, non_exam_score, exam_score):
    if is_file_empty(TARGET_DIR):
        df = pd.read_csv(TARGET_DIR)
    else:
        df = pd.DataFrame({
            "student_id": student_id,
            "non_exam_score": non_exam_score,
            "exam_score": exam_score
        })
    
    students = df["student_id"]

    is_matched = False
    for student in students:
        if student == student_id:
            is_matched = True
    
    if is_matched:
        raise StudentAlreadyExistsError(f"Student with the ID {student_id} already exists")
    else:
        new_student = {
            "student_id": student_id,
            "non_exam_score": non_exam_score,
            "exam_score": exam_score
        }
        df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)


def delete_student(studnet_id):
    if is_file_empty(TARGET_DIR):
        raise EmptyDatabaseError("The database is empty please add a student before deleting it.")


