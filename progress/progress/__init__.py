from progress.check.check import check_activation

check_activation()

from .analyse import (
    set_student,
    remove_student,
    change_exam_grade,
    change_coursework_grade,
    add_student,
    analyse_student,
    show_grades,
    average_class_grades,
    student_grades
)

__all__ = [
    "set_student",
    "remove_student",
    "change_exam_grade",
    "change_coursework_grade",
    "add_student",
    "analyse_student",
    "show_grades",
    "average_class_grades",
    "student_grades"
]