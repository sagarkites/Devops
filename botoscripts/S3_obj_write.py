import boto3 
s3 = boto3.resource('s3')
content = s3.Object('pichai', 'some.py').put(Body = open('/Users/pavanscott/Documents/botoscripts/Ec2_list.py', 'rb'))
print(content)