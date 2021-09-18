FROM amazon/aws-lambda-python

RUN yum install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm awscliv2.zip
RUN rm -rf ./aws

WORKDIR ${LAMBDA_TASK_ROOT}

COPY main.py ${LAMBDA_TASK_ROOT}

RUN mkdir ./python_modules
RUN pip install --upgrade pip
RUN pip install awslambdaric -t ./python_modules/
RUN pip install aws-wsgi -t ./python_modules/


RUN export PYTHONPATH="$PYTHONPATH:$LAMBDA_TASK_ROOT/src"
