# Student Grader
This is a Python applicaiton for programming lab that calculates students' grades based on assignmet scores and exam results. The project demonstrates Python logic.

## Features

### Core Grading Feature
- Functions to calculate min, max, and maximum scores.
- Final grade calculation based on configurable grading rules.
- Pass/fail determination.

### Services
- Manuel entry of students and grades though service layer.
- Import of students and grades from Excel files.
- Adapter pattern to normalzie external data formats into internal models.
- Input validation before grade processing.

### Third-party usage simulation
- Python client interface for third-party developers.
- High-level methods can be used for various services.
- Development-time authorization.
- Student progression analysis.

### Architecture Design
- Clear separation between logic, servies, and client layers.
- Service-priented architecture without requiring a web server.
- Allows future integration with a web API.


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