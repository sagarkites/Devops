import boto3
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
list = ec2.describe_instances()
for i in list["Reservations"]:
    j = [sagar["InstanceId"] for sagar in i["Instances"]]
    k = [chanti["State"] for chanti in i["Instances"]]
    l = k[0]
    res ="The Instanes are: {} and they are {}".format(j,l["Name"])
    print(res)
    
