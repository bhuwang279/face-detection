# the future is now!
FROM python:3.6
ENV LANG C.UTF-8

LABEL maintainer="cto@bhutanbuy.com"

RUN mkdir /face_compare_api

RUN apt-get -y update
# This is a sample Dockerfile you can modify to deploy your own app based on face_recognition

FROM python:3.6-slim-stretch

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    python3 \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-base-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS


ADD requirements.txt /face_compare_api/requirements.txt

RUN pip3 install -r /face_compare_api/requirements.txt
RUN apt-get -y update && apt-get -y autoremove

WORKDIR /face_compare_api

EXPOSE 8000

CMD gunicorn -b :8000 face_compare_api.wsgi