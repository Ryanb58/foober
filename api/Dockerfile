FROM python:3.6.5-alpine

ARG dev

WORKDIR /app

COPY ./wait-for.sh /
RUN chmod 755 /wait-for.sh

COPY ./requirements.txt requirements.txt

RUN apk add --no-cache build-base postgresql-dev git && \
    set -ex && pip install -r requirements.txt && \
    apk del --purge build-base

COPY . .
COPY ./start.sh /start.sh
RUN chmod 755 /start.sh

ENTRYPOINT [ "/wait-for.sh", "db:5432", "--" ]