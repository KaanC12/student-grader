import pandas as pd
import os
from student_grader.exceptions import EmptyDatabaseError

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(DIR_PATH, "..", "data", "students.csv")

class StudentStatistics:
    def __init__(self):
        if os.path.getsize(CSV_PATH) == 0:
            raise EmptyDatabaseError("The database is empty please add students first.")
        else:
            self.df = pd.read_csv(CSV_PATH)
    
    def final_score(self, student_id):
        exam_score = self.df.loc(student_id, "exam_score")
        non_exam_score = self.df.loc(student_id, "non_exam_score")
        return exam_score + non_exam_score