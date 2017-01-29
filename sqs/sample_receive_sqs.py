"""
sample AWS SQS dequeue an item
"""
import boto3    # AWS module
import json

# open a connection to the SQS service
sqs = boto3.resource('sqs')

#for queue in sqs.queues.all():
#    print(queue.url)

# create (or return existing) queue of this name
try:
    queue = sqs.get_queue_by_name(QueueName='sample_queue')
except:
    queue = sqs.create_queue(QueueName='sample_queue', Attributes={'DelaySeconds': '5'})
print(queue.url)

# format the message
expectedMsg = """
{
    "verb": "SCAN",
    "TCPIP": "97.80.230.155"
}
"""
expectedPayload = json.loads(expectedMsg)
expectedJsonMsg = json.dumps(expectedPayload)
print('Expected message:        "{0}"'.format(expectedMsg))
print('Expected Msg json.loads: "{0}"'.format(expectedPayload))
print('Expected Msg json.dumps: "{0}"'.format(expectedJsonMsg))

# receive the message
messages = queue.receive_messages(MaxNumberOfMessages=10,WaitTimeSeconds=5,
    AttributeNames=['All'],MessageAttributeNames=['*'])
for msg in messages:
    print('Received msg body:       "{0}"'.format(msg.body))
    print('Received body attr:      "{0}"'.format(msg.attributes))
    print('Received msg attr:       "{0}"'.format(msg.message_attributes))
    #assert expectedJsonMsg == msg.body
    # by acknowledging message was processed, it will be removed from queue
    # otherwise, after "Default Visibility Timeout", it becomes visible again
    response = msg.delete()
    print('Response msg delete:     "{0}"'.format(response))
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

# let's delete the temporary queue 'sample_queue' we created
# remember if you attempt to create same queue name within 60 seconds,
# this new create is expected to fail according to SQS docs.
client = boto3.client('sqs')
response = client.delete_queue(QueueUrl=queue.url)
print('Response queue delete:   "{0}"'.format(response))
assert response['ResponseMetadata']['HTTPStatusCode'] == 200

