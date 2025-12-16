import pandas as pd
import os
from student_grader.exceptions import EmptyDatabaseError

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(DIR_PATH, "..", "data", "students.csv")

# Error Messages
DATABASE_IS_EMPTY = "The database is empty please add students first"

class StudentStatistics:
    def __init__(self):
        if os.path.getsize(CSV_PATH) == 0:
            raise EmptyDatabaseError(DATABASE_IS_EMPTY)
        else:
            self.df = pd.read_csv(CSV_PATH, index_col="student_id")
    
    def final_score(self, student_id):
        exam_score = self.df.loc(student_id, "exam_score")
        non_exam_score = self.df.loc(student_id, "non_exam_score")
        return exam_score + non_exam_score
    
    def exam_score(self, student_id):
        return self.df.loc(student_id, "exam_score")
    
    def non_exam_score(self, student_id):
        return self.df.loc[student_id, "non_exam_score"]
    
    def average_score(self, student_id):
        return self.final_score(student_id) / 2
    
    def score_delta(self, student_id):
        return self.exam_score(student_id) - self.non_exam_score(student_id)
