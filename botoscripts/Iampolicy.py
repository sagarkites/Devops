import boto3
import json
iam = boto3.client('iam')
response = iam.create_user(UserName = 'sagarscott' )
print(response)
policy = {}
response = iam.create_policy(PolicyName = 'Policy', PolicyDocument=json.dumps('policy'))
print(response)
