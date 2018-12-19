import boto3
s3 = boto3.client('s3')
List = s3.list_buckets()
buckets = [storage['Name'] for storage in List['Buckets']]
print(buckets)
bucket creation = s3.create_bucket(Bucket = 'jiraya')
print(bucket_creation)
upload = s3.upload_file('/Users/pavanscott/Documents/Aws_Boto/Bucket.py','jiraya','Bucket.py')
print(upload)
