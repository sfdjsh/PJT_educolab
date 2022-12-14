FROM python:3.9.5
WORKDIR /var/jenkins_home/workspace/educolab_back/
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get install -y redis-server
COPY . .
WORKDIR /var/jenkins_home/workspace/educolab_back/backend
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "educolab.wsgi:application"]
# EXPOSE 8000