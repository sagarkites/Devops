import boto3
import json
# Bucket Policy
s3 = boto3.client('s3')
Bucket_policy = {
               "Version":"2012-10-17",
                "Statement":[{"Sid":"AddPerm",
                              "Effect":"Allow",
                              "Principal": "*",
                              "Action":["s3:GetObject"],
                              "Resource":["arn:aws:s3:::sagarscott/*"]
                }
            ]
        }
print(Bucket_policy)                               
Serial = json.dumps(Bucket_policy)
print(Serial)
result = s3.put_bucket_policy(Bucket='sagarscott', Policy=Serial)
get = s3.get_bucket_policy(Bucket = 'sagarscott')
print(get)
