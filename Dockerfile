FROM python:3.6
LABEL maintainer @nataliasudar

#RUN apt-get -qq -y update
#RUN apt-get -y install cron rsyslog vim && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/code
COPY code/*.py ./
RUN pip3 install -r requirements.txt

RUN useradd app
RUN chown app:app -R ../code

CMD python3 app.py
