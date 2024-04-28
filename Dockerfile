FROM python:3-alpine

RUN mkdir /opt/build
RUN apt update
RUN apt install gcc -y

COPY biggie.py /opt/biggie.py
COPY run.sh /opt/run.sh
COPY even_biggier.c /opt/build

RUN gcc -o /opt/even_biggier /opt/build/even_biggier.c


CMD ["/opt/run.sh"]