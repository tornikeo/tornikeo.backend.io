FROM python:3.10-slim-buster
WORKDIR /code
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
WORKDIR /code/app/
COPY src src
COPY .env .
EXPOSE ${PORT}
ENTRYPOINT uvicorn src.main:app --host 0.0.0.0 --port ${PORT}
