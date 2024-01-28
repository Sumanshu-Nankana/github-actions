FROM python:3.11-alpine

WORKDIR /app

COPY src /app/src

ENTRYPOINT ["python", "src/app.py"]


# Build: docker build -t my-python-app .
# Run:  docker run --rm my-python-app 1 2 3 4