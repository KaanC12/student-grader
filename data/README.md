# Data Directory
This directory contains CSV files used to simulate data storage and third-party
access for the project.

The aim of the data files is to simulate a real database. Therefore, no real
database or server is used in this project.

# student.csv
Stores student grades and their information used by the grading service.

### Purpose
- Acts as a lightweight data store for student scores and clients

### Example Structure

```bash
student_id, ,non-exam_score, exam_score
123, 80, 90
124, 70, 95
```

##### Column Description
- `student_id`: Unique identifier for the student.
- `non-exam_score`: Scores of presentations, quizes, etc.
- `exam_scores`: Scores of exams.

# client.csv
Stores API keys used to simulate third-party authorizaiton.

### Purpose
- Simulates client authentication without a real server.

### Example Structure

```bash
client_name, api_key, active
kaan, 1234, true
ahmet, 1235, false
```

##### Column Description
- `client_name`: Identifier for the client or developer.
- `api_key`: API key used for activation.
- `active`: Indicates whether the client is allowed to use the system.

# Notes
These CSV files are not secure and are used only to simulate authentication.
The project is designed so that these files could be replaced by a real database
or API without changing the main logic.