FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /omdb_backend
WORKDIR /omdb_backend
COPY requirements.txt /omdb_backend/
RUN pip install -r requirements.txt
COPY . /omdb_backend/