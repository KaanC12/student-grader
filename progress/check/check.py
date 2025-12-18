import os
from student_grader.exceptions.exceptions import ActivationError

# Error Message
IN_ACTIVE = "Progress is not activated. \n Run: source scripts/activate <clilent_name> <api_key>"

def check_activation():
    if os.environ.get("STUDENT_GRADER_ACTIVE") != "1":
        raise ActivationError(IN_ACTIVE)
