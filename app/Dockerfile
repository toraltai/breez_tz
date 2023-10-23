FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python3 manage.py collectstatic --no-input