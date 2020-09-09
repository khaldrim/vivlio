FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN apt-get install \
     git &&\
     python3 -m pip install --upgrade pip &&\
     python3 -m pip install --no-cache-dir -r requirements.txt
COPY . /src/