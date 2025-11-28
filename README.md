# Student Grader
This is a Python applicaiton for programming lab that calculates students' grades based on assignmet scores and exam results. The project demonstrates Python logic.

## Features
- Adapter pattern to convert students grades in excel format into a dict.
- Functions to find average, minimum, and maximum scores.
- Function to find final grade.
- Function to find the student's progression.
- Determine whether a student passes or fails.

## Clean Code Guidelines
- Please follow the PEP 8 style guide.
- Lines should not exceed 80 characters.
- Use meaningful variable and function names.
- Keep functions small and focused on a single task.
- Add comments only when necessary: clean code should be self-explanatory.

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

While adding commit descriptions please use conventional commits.

```bash
    feat: add grade calculation function # add new feature to the project.
    fix: correct wrong logic # use for bug fixes/issues
    docs: update README with convenvtional commits. # For documentations.
    build: add Dockerfile # everything related to build pipeline.
    chore: update .gitignore # Update dependencies.
    style: fix whitespaces # Code changes but the logic does not.
    refactor: simplify grade calculation loop # Make the code cleaner.
    test: add tests # Add unit test and integration test etc.
    perf: optimize grade calculation to reduce runtime # Optimizes the code.
    revert: revert a commit. # Reverts a commit.
```