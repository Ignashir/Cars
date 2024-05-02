FROM python:3.12
EXPOSE 8000
LABEL authors="ignacyhirsz"

ENV PYTHONDONTWRITEBYBYTECODE 1
ENV PYTHONUNBUFERED 1

WORKDIR /webapp
COPY Pipfile Pipfile.lock /webapp/

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . /webapp/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]