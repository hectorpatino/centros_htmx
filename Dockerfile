FROM python:3.9.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    python3-gdal

WORKDIR /app

COPY . /app/
RUN pip install -r /app/requirements.txt


