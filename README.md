# Student Grader
This is a Python applicaiton for programming lab that calculates students' grades based on assignmet scores and exam results. The project demonstrates Python logic.


## Features

## How to Run
- Please install docker and a engine. See docker website. 

### Run 
If you are using Colima:

```bash
    colima start
    docker build -t start-grader .
    docker run --rm student-grader
```

You can stop it by using `colima stop`

### Push to Repository
**Please do NOT push directly to the `main` branch. Create a new branch based on your role, then open a Pull Request on GitHub.**

```bash
    git add . # Stage all changes.
    git commit -m "Describe your changes." # Commit them
    git checkout -b feature/grade-calculation # Create and switch to a new branch
    git push -u origin feature/grade-calculation # Push the new branch to Git
```