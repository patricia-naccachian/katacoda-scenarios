FROM python:3.7

RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [“python3”]

CMD [“python","app.py”]