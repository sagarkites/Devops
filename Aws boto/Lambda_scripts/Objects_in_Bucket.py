import boto3
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    list = s3.list_objects_v2(Bucket = 'pichai')
    bucket_objs = [i['Key'] for i in list['Contents']]
    print(bucket_objs)