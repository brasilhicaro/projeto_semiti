FROM python:3.11-buster

ADD . /projeto_semiti

WORKDIR /projeto_semiti

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
