# Dockerfile, Image, Container
FROM python:latest
ADD motor.py .
ADD app.py .
RUN pip install requests
RUN pip install flask
CMD ["python","-u","app.py"]
