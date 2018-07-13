FROM postgres:10

COPY ./schema/* /docker-entrypoint-initdb.d/
