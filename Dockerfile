FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code/app
COPY ./app /code/app

# Copy .env file as well (temporary fix, I guess)
COPY .env .
RUN pip install python-dotenv
ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port ${PORT}
