# Dockerfile, Image, Container
FROM python:latest
ADD motor.py .
ADD app.py .
ADD /templates/index.html  ./templates/index.html
ADD /logs/debug.log  ./logs/debug.log
RUN pip install requests
RUN pip install flask
ARG BUILDTAG
ENV BUILDTAG=$BUILDTAG
CMD ["python","-u","app.py"]
