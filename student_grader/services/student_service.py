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
    return (not os.path.exists(path)) or os.path.getsize(path) == 0

def add_student(*, student_id, non_exam_score: float, exam_score: float):
    new_student = {
            "student_id": student_id,
            "non_exam_score": non_exam_score,
            "exam_score": exam_score
        }
    
    if is_file_empty(TARGET_DIR):    
        df = pd.DataFrame([new_student])
        df = df.set_index("student_id")
        df.index.name = "student_id"
        df.to_csv(TARGET_DIR)
    else:
        df = pd.read_csv(TARGET_DIR, index_col="student_id")

        if student_id in df.index:
            raise StudentAlreadyExistsError(
                STUDENT_ALREADY_EXIST.format(student_id=student_id)
            )

        df.loc[student_id] = {
            "non_exam_score": non_exam_score,
            "exam_score": exam_score
        }
        df.index.name = "student_id"
        df.to_csv(TARGET_DIR)

def change_exam_score(student_id, new_score):
    if is_file_empty(TARGET_DIR):
        raise EmptyDatabaseError(DATABASE_EMPTY)
    else:
        df = pd.read_csv(TARGET_DIR, index_col="student_id")
        df.loc[student_id, "exam_score"] = new_score

def change_non_exam_score(student_id, new_score):
    if is_file_empty(TARGET_DIR):
        raise EmptyDatabaseError(DATABASE_EMPTY)
    else:
        df = pd.read_csv(TARGET_DIR, index_col="student_id")
        df.loc[student_id, "non_exam_score"] = new_score

def delete_student(student_id):
    if is_file_empty(TARGET_DIR):
        raise EmptyDatabaseError(DATABASE_EMPTY)
    else:
        df = pd.read_csv(TARGET_DIR, index_col="student_id")
        if student_id not in df.index:
            raise ValueError("Student not found")
        
        df = df.drop(student_id)
        df.to_csv(TARGET_DIR)


def import_students_from_excel(file_path: str):
    try:
        df_excel = pd.read_excel(file_path).set_index("student_index")
        df_excel.index.name = "student_id"
    except (FileNotFoundError, ValueError) as e:
        raise ExcelError("Invalid excel file") from e
    
    if is_file_empty(TARGET_DIR):
        df_excel.to_csv(TARGET_DIR)
    else:
        df_csv = pd.read_csv(TARGET_DIR, index_col="student_id")
        df_combined = pd.concat([df_csv, df_excel])
        df_combined = df_combined[~df_combined.index.duplicated(keep="first")] 
        df_combined.to_csv(TARGET_DIR)

