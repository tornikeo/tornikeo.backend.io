FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code/app
COPY ./app /code/app
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port ${PORT}
