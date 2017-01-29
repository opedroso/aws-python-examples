"""
sample AWS SQS enqueue an item
"""
import boto3    # AWS API python module
import json

# open a connection to the SQS service
# (using ~/.aws/credentials for access info)
sqs = boto3.resource('sqs')

# print queues in existence
#for queue in sqs.queues.all():
#    print(queue.url)

# create (or return existing) queue of this name
try:
    queue = sqs.get_queue_by_name(QueueName='sample_queue')
except:
    try:
        queue = sqs.create_queue(QueueName='sample_queue', Attributes={'DelaySeconds': '5'})
    except:
        # print exception in case sqs could not create the queue
        import sys, traceback, uuid, datetime
        # API is "exc_traceback = sys.exc_info(out exc_type, out exc_value)"
        # next stmt: out parameters come before equal return variable
        exc_type, exc_value, exc_traceback = sys.exc_info()
        e = traceback.format_exception(exc_type, exc_value, exc_traceback)
        e = ''.join(e)
        uniqueErrorId = uuid.uuid4()
        data = {'status': 'E', 'uuid': uniqueErrorId, 'exception': str(e), 'now': datetime.datetime.utcnow()}
        print("Exception caught during SQS.create_queue: '{0}'".format(data))
        sys.exit(0) # forces script exit without a traceback printed

# print queue url for diagnostics
print(queue.url)

    
# on a real program, one would not purge the queue, but here is how to do it
try:
    queue.purge()
except:
    # only purge once every 60 seconds allowed in SQS...
    pass    # <<== this is a noop stmt in python; this will "eat" the exception and continue execution

# format the message to be sent
msgBody = """
{
    "verb": "SCAN",
    "TCPIP": "97.80.230.155"
}
"""
print ('orignal msg:              "{0}"'.format(msgBody))
body = json.loads(msgBody)
print('msg body after json.loads: "{0}"'.format(json.dumps(body)))

# send the message
string_msg = json.dumps(body)
string_msgAttributes = {
    'Author': {
        'StringValue': __file__,    # <== "sample_post_sqs.py"
        'DataType': 'String'
    }
}
try:
    queue.send_message(MessageBody=string_msg,
                       MessageAttributes=string_msgAttributes)
except:
    import sys, traceback, uuid, datetime
    # API is "exc_traceback = sys.exc_info(out exc_type, out exc_value)"
    # next stmt: out parameters come before equal return variable
    exc_type, exc_value, exc_traceback = sys.exc_info()
    e = traceback.format_exception(exc_type, exc_value, exc_traceback)
    e = ''.join(e)
    uniqueErrorId = uuid.uuid4()
    data = {'status': 'E', 'uuid': uniqueErrorId, 'exception': str(e), 'now': datetime.datetime.utcnow()}
    print("Exception caught during SQS.create_queue: '{0}'".format(data))
    sys.exit(0) # forces script exit without a traceback printed

