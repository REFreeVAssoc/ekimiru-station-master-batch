FROM python:3.8-slim
WORKDIR /service
COPY main.py /service/

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less curl

RUN mkdir ./python_modules
RUN pip install --upgrade pip
# google cloud
RUN pip install google-cloud
RUN pip install functions-framework

RUN export PYTHONPATH="$PYTHONPATH:/service/src"

EXPOSE 8010

CMD ["/bin/sh"]
