FROM python:3.6

RUN pip install --upgrade pip boto3 uuid

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy source
COPY . /usr/src/app

CMD ["python", "test.py"]
