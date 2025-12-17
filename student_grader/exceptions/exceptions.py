class StudentAlreadyExistsError(Exception):
    """Raised an error when a student with the given ID already exists."""

class EmptyDatabaseError(Exception):
    """Raised an error when the file is empty."""

class ExcelError(Exception):
    """Base exception for Excel import errors."""