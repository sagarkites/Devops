import boto3
import time
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')
s3 = boto3.resource('s3')
obj = s3.Object('pichai', 'Ec2.txt')
r = obj.get()['Body'].read().decode('utf-8')
print(r)
#instance = ec2.Instance(r).start()
