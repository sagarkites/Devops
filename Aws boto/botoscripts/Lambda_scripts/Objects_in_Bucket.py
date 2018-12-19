import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    obj = s3.Object('pichai', 'boto.pem')
    print(obj.get()['Body'].read().decode('utf-8'))
