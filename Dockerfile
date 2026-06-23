FROM python:3.11-alpine
WORKDIR /app
RUN pip install flask
COPY main.py .
CMD ["python", "main.py"]
