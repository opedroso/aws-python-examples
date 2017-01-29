The samples contained can be run by executing the following command:

$ python3 [filename]

# REQUIREMENTS

## AWS account information

Prior to doing this successfully though, you will need to get an AWS account and create the following two files:

### This is your default region where your AWS resources will be created

C:\Users\Administrator>type .aws\config   # if you are using Linux, ~/.aws/config</br>
[default]</br>
region=us-east-1</br>


### This is your credential for accessing AWS

C:\Users\Administrator>type .aws\credentials   # if you are using Linux, ~/.aws/credentials</br>
[default]</br>
aws_access_key_id=I5id744YHEI2BJQXYZZY</br>
aws_secret_access_key=TPQ7Amw7sucfk1FocaF0faIvZar2BVmPrF93QZmN</br>

You can find the information needed for the credentials file by clicking your name on the AWS main console and selecting "My Security Credentials".</br>
Click on "Account Identifiers" to view your AWS Account ID.</br>
Click on "Access Keys (Access Key ID and SecretAccessKey") to view your access keys. If you don't have one, create one. Follow best practices on AWS as directed per their site.</br>

## Software Requirements

- Install python3 (https://www.python.org/downloads/)
- install boto3   (https://pypi.python.org/pypi/boto3)
Note: if new major version is latest available, you may save some grief by selecting previous latest version, since most likely boto3 was not built with very latest version.

# Example

### Get example code

$ git clone https://github.com/opedroso/aws-python-examples.git</br>
$ cd aws-python-examples</br>
$ cd sqs</br>


### Creates a queue named "sample_queue" and post a single message to it


$ python sample_post_sqs.py<br>
https://queue.amazonaws.com/628650250372/sample_queue<br>
orignal msg:              "<br>
{<br>
    "verb": "SCAN",<br>
    "TCPIP": "97.80.230.155"<br>
}<br>
"<br>
msg body after json.loads: "{"TCPIP": "97.80.230.155", "verb": "SCAN"}"<br>

### Read and print the message(s) contained in "sample_queue", deleting the queue once done

$ python sample_receive_sqs.py<br>
https://queue.amazonaws.com/628650250372/sample_queue<br>
Expected message:        "<br>
{<br>
    "verb": "SCAN",<br>
    "TCPIP": "97.80.230.155"<br>
}<br>
"<br>
Expected Msg json.loads: "{'verb': 'SCAN', 'TCPIP': '97.80.230.155'}"<br>
Expected Msg json.dumps: "{"verb": "SCAN", "TCPIP": "97.80.230.155"}"<br>
Received msg body:       "{"TCPIP": "97.80.230.155", "verb": "SCAN"}"<br>
Received body attr:      "{'ApproximateFirstReceiveTimestamp': '1485700808845', 'SentTimestamp': '1485700725029', 'ApproximateReceiveCount': '1', 'SenderId': '628698750372'}"<br>
Received msg attr:       "{'Author': {'StringValue': 'sample_post_sqs.py', 'DataType': 'String'}}"<br>
Response msg delete:     "{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '53816aec-84c0-509a-9330-3be485c87014', 'RetryAttempts': 0, 'HTTPHeaders': {'content-length': '215', 'date': 'Sun, 29 Jan 2017 14:40:08 GMT', 'connection': 'keep-alive', 'x-amzn-requestid': '53816aec-84c0-509a-9330-3be485c87014', 'server': 'Server', 'content-type': 'text/xml'}}}"<br>
Response queue delete:   "{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '98ff1549-4265-52da-a042-4441436cb29c', 'RetryAttempts': 0, 'HTTPHeaders': {'content-length': '211', 'date': 'Sun, 29 Jan 2017 14:40:09 GMT', 'connection': 'keep-alive', 'x-amzn-requestid': '98ff1549-4265-52da-a042-4441436cb29c', 'server': 'Server', 'content-type': 'text/xml'}}}"<br>

### Rerun the post.

If done within 60 seconds, you will exercise a custom exception handler, since AWS queues cannot be created with the same name within 60 seconds of being deleted.

$ python sample_post_sqs.py


