FROM python:latest

RUN apt-get update && apt-get install --yes --no-install-recommends




WORKDIR /

COPY main.py /main.py
COPY files /files
COPY requirements.txt /requirements.txt


RUN pip --no-cache-dir install -r requirements.txt


CMD ["python", "main.py"]