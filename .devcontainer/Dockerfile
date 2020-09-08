FROM python:3.8-alpine
RUN apk add --no-cache --purge -uU mysql mysql-client mariadb-dev mariadb-connector-c
RUN apk add --no-cache --virtual build-deps gcc musl-dev
RUN rm -rf /var/cache/apk/* /tmp/*
RUN pip install flask flask_sqlalchemy flask_marshmallow marshmallow-sqlalchemy mysqlclient pyjwt flask-cors
RUN apk del build-deps mariadb-dev
EXPOSE 3306
