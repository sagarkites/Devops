import boto3
s3 = boto3.client('s3')
list = s3.list_objects_v2(Bucket = 'pichai')
bucket_objs = [i['key'] for i in list['contents']]
print(bucket_objs)