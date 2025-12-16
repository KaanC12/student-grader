import os
import pandas as pd
from student_grader.exceptions import StudentAlreadyExistsError, EmptyDatabaseError, ExcelError

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER_DIR = CURRENT_DIR[:len(CURRENT_DIR) - 1 - len("services")]
TARGET_DIR = os.path.join(FOLDER_DIR, "data", "students.csv")

# Error Messages
STUDENT_ALREADY_EXIST = "Student with the ID {student_id} already exists"
DATABASE_EMPTY = "The database is empty please add a student before deleting it."

def is_file_empty(path):
    if os.path.getsize(path) > 0:
        return True
    else:
        return False

def add_student(*, student_id, non_exam_score: float, exam_score: float):
    if not is_file_empty(TARGET_DIR):
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
        raise StudentAlreadyExistsError(STUDENT_ALREADY_EXIST.format(
            student_id=student_id
        ))
    else:
        new_student = {
            "student_id": student_id,
            "non_exam_score": non_exam_score,
            "exam_score": exam_score
        }
        df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
        df.to_csv(TARGET_DIR, index=False)


def delete_student(studnet_id):
    if not is_file_empty(TARGET_DIR):
        raise EmptyDatabaseError(DATABASE_EMPTY)
    else:
        df = pd.read_csv(TARGET_DIR)
        df = df[df["student_id"] != studnet_id]
        df.to_csv(TARGET_DIR, index=False)


def import_students_from_excel(file_path: str):
    try:
        df_excel = pd.read_excel(file_path)
    except (FileNotFoundError, ValueError) as e:
        raise ExcelError("Invalid excel file") from e
    
    if not is_file_empty(TARGET_DIR):
        df_excel.to_csv(TARGET_DIR)
        return
    else:
        df_csv = pd.read_csv(TARGET_DIR)
        df_combined = pd.concat([df_csv, df_excel], ignore_index=True)
        df_combined.to_csv(TARGET_DIR, index=False)