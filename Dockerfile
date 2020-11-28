FROM python:3.6-alpine

RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre

WORKDIR /home/Plataforma
COPY app app
COPY requirements.txt requirements.txt
COPY migrations migrations
COPY application.py application.py
COPY wsgi.py wsgi.py 
COPY wsgi.ini wsgi.ini
COPY config.py config.py

ENV SECRET_KEY = SECRET_KEY
ENV SQLALCHEMY_DATABASE_URI= SQLALCHEMY_DATABASE_URI 
ENV BUCKET_NAME= BUCKET_NAME

RUN pip install -r requirements.txt

RUN apk del .build-dependencies && rm -rf /var/cache/apk/*

EXPOSE 5000
CMD ["uwsgi", "--ini", "wsgi.ini"]