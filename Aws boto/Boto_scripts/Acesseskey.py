import boto3
#Creating Accesskey
iam = boto3.client('iam')
accesskey = iam.create_access_key(UserName='sagar')
print(accesskey['Accesskey'])
