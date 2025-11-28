# 1. Lightweight base image.
FROM python:3.13.3-slim

# 2. Working directory.
WORKDIR /app

# 3. Copy files of the project.
COPY . .

# 4. Start application.
CMD [ "python", "-m", "main"]