FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV UVICORN_CMD="uvicorn app.main:app --host 0.0.0.0 --port 80 --reload"

CMD ["sh", "-c", "$UVICORN_CMD"]