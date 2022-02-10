FROM python:3-alpine

COPY biggie.py /opt/biggie.py
COPY run.sh /opt/run.sh

CMD ["/opt/run.sh"]