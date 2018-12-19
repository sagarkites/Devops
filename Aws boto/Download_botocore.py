import boto3
import botocore
s3 = boto3.resource('s3')
try:
	download = s3.Bucket('sagarscott').download_file('Bucket.py','ok.py')
except botocore.exceptions.ClientError as e:
     if e.response['Error']['code'] == '404':
             print('Your Object in S3 Has Issues')
     else:
           raise   	