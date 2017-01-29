The samples contained can be run by executing the following command:

$ python3 [filename]

REQUIREMENTS
============

AWS account information

Prior to doing this successfully though, you will need to get an AWS account and create the following two files:

# this is your default region where your AWS resources will be created
'''
C:\Users\Administrator>type .aws\config   # if you are using Linux, ~/.aws/config
[default]
region=us-east-1
'''

# this is your credential for accessing AWS
'''
C:\Users\Administrator>type .aws\credentials   # if you are using Linux, ~/.aws/credentials
[default]
aws_access_key_id=I5id744YHEI2BJQXYZZY
aws_secret_access_key=TPQ7Amw7sucfk1FocaF0faIvZar2BVmPrF93QZmN
'''

You can find the information needed for the credentials file by clicking your name on the AWS main console and selecting "My Security Credentials".
Click on "Account Identifiers" to view your AWS Account ID.
Click on "Access Keys (Access Key ID and SecretAccessKey") to view your access keys. If you don't have one, create one. Follow best practices on AWS as directed per their site.

Software Requirements

- Install python3 (https://www.python.org/downloads/)
- install boto3   (https://pypi.python.org/pypi/boto3)
Note: if new major version is latest available, you may save some grief by selecting previous latest version, since most likely boto3 was not built with very latest version.

Example
=======

# get example code
'''
$ git clone https://github.com/opedroso/aws-python-examples.git
$ cd aws-python-examples
$ cd sqs
'''

# creates a queue named "sample_queue" and post a single message to it
'''
$ python sample_post_sqs.py
'''

# read and print the message(s) contained in "sample_queue", deleting the queue once done
'''
$ python sample_receive_sqs.py
'''

# rerun the post. If done within 60 seconds, you will exercise a custom exception handler, since AWS queues cannot be created with the same name within 60 seconds of being deleted.
'''
$ python sample_post_sqs.py
'''

