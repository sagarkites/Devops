import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('pichai')
list_objects = [object.key for object in bucket.objects.filter(Delimiter = '/')]
print(list_objects)
