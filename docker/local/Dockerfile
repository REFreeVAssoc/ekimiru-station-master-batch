FROM python:3.8-slim

WORKDIR /service

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install pytest
RUN export PYTHONPATH="$PYTHONPATH:/service"

EXPOSE 8000

CMD ["/bin/sh"]
