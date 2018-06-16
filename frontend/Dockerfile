FROM node:10.2.1-alpine

ARG dev

COPY ./wait-for.sh /wait-for.sh
RUN chmod 755 /wait-for.sh

ADD ./package.json /app/

WORKDIR /app

RUN npm install

ENTRYPOINT [ "/wait-for.sh", "api:8000", "--" ]
