FROM amazon/aws-lambda-python

COPY main.py ${LAMBDA_TASK_ROOT}

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install awslambdaric
RUN pip install aws-wsgi
RUN yum install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install
RUN rm awscliv2.zip
RUN rm -rf ./aws
