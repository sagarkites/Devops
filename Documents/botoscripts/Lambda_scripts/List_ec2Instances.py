import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    list = ec2.describe_instances()
    for i in list["Reservations"]:
        j = [sagar["InstanceId"] for sagar in i["Instances"]]
        k = [chanti["State"] for chanti in i["Instances"]]
        l = k[0]
        print("The Instance_id {0} is {1}".format(j,l["Name"]))
