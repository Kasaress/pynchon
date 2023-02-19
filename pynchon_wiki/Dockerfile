FROM python:3.7-slim

WORKDIR /app

COPY .. .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "pynchon_wiki.wsgi:application", "--bind", "0:8000" ]