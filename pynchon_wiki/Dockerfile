FROM python:3.7-slim

WORKDIR /app


RUN apt-get update && \
    apt-get install vim -y --no-install-recommends

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "pynchon_wiki.wsgi:application", "--bind", "0:8000" ]