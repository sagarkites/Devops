import boto3
#Getting SGP info
ec2 = boto3.client('ec2')
Group = ec2.describe_security_groups()
print(Group['SecurityGroups'])
