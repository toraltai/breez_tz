FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]