FROM python:3.11.5

ENV PYTHONBUFFERED=1

WORKDIR /pizza

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python3 manage.py runserver 0.0.0.0:8000