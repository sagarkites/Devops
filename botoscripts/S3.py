import boto3 
# Downloding file from S3
s3 = boto3.client('s3')
s3_get = s3.download_file('jiraya','Bucket.py', '/Users/pavanscott/Downloads/script.py')
print(s3_get)