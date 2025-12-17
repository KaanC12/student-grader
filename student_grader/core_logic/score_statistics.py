import pandas as pd
import os
from student_grader.exceptions import EmptyDatabaseError

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(DIR_PATH, "..", "data", "students.csv")

# Error Messages
DATABASE_IS_EMPTY = "The database is empty please add students first"

class StudentStatistics:
    def __init__(self):
        if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
            raise EmptyDatabaseError(DATABASE_IS_EMPTY)
        else:
            self.df = pd.read_csv(CSV_PATH, index_col="student_id")
    
    def final_score(self, student_id):
        exam_score = self.df.loc[student_id, "exam_score"]
        non_exam_score = self.df.loc[student_id, "non_exam_score"]
        return exam_score + non_exam_score
    
    def exam_score(self, student_id):
        return self.df.loc[student_id, "exam_score"]
    
    def non_exam_score(self, student_id):
        return self.df.loc[student_id, "non_exam_score"]
    
    def average_score(self, student_id):
        return self.final_score(student_id) / 2
    
    def score_delta(self, student_id):
        return self.non_exam_score(student_id) - self.exam_score(student_id)
    
    def is_passing(self, student_id) -> bool:
        ratio_non_exam_score = self.non_exam_score(student_id) * 40 / 100
        ratio_exam_score = self.exam_score(student_id) * 60 / 100

        return ratio_non_exam_score + ratio_exam_score >= 40


class CohortStatistics:
    def __init__(self):
        if not os.path.exists(CSV_PATH) or os.path.getsize(CSV_PATH) == 0:
            raise EmptyDatabaseError(DATABASE_IS_EMPTY)
        else:
            self.df = pd.read_csv(CSV_PATH, index_col="student_id")

    def exam_average(self):
        return self.df["exam_score"].mean()

    def coursework_average(self):
        return self.df["non_exam_score"].mean()

    def exam_notes(self) -> list:
        return self.df["exam_score"].to_list()

    def coursework_notes(self) -> list:
        return self.df["non_exam_score"].to_list()
    
    def has_passed(self) -> list:
        passed_ids = self.df[
            (self.df["non_exam_score"] * 0.4 + self.df["exam_score"] * 0.6) >= 40
        ].index.to_list()

        return passed_ids