import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('pichai')
list_obj = [object.key for object in bucket.objects.filter(Delimiter = '/')]
list_buckets = [object.bucket_name for object in bucket.objects.filter(Delimiter = '/')]
print("The Buckets are {} Objects are {} ".format(list_buckets[0], list_obj))
