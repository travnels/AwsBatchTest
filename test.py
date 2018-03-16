import json
import urllib.parse
import boto3
import uuid

print('Loading function')

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='tnelson-test.fifo')

try:
    for x in range(0, 300000):
        queue_response = queue.send_message(
            MessageBody=str(x),
            MessageGroupId=uuid.uuid4().hex
        )

except Exception as e:
    print(e)
    raise e
