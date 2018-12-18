import boto3
import os
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    sns = boto3.client('sns')
    evar = os.environ["ARN"]
    list = ec2.describe_instances()
    for i in list["Reservations"]:
        j = [temp["InstanceId"] for temp in i["Instances"]]
        k = [temp3["State"] for temp3 in i["Instances"]]
        l = k[0]
        if l["Name"] == "running":
           shutdown = (ec2.stop_instances(InstanceIds=j))
           response = "The Instance with instance-id {} is stopped".format(j)
           print(response)
           pub = sns.publish(TopicArn = evar,
                             Message = response)
