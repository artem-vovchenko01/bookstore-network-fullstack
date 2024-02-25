FROM python:latest

WORKDIR /usr/src/app

RUN pip install fastapi
RUN pip install uvicorn[standard]
RUN pip install mariadb
RUN pip install python-multipart
RUN mkdir -p /data/books/covers

COPY ./app .

ENV PYTHONUNBUFFERED=1

CMD ["python", "-u", "main.py"]

