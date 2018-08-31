import boto3
import os
def lambda_handler(event, context):
    x = os.environ['TAG']
    ec2 = boto3.resource('ec2')
    for i in ec2.instances.all():
        tag = [i.id for t in i.tags if t['Value'] == x]
        for k in tag:
            instance = ec2.Instance(k).start()
            print(instance)
