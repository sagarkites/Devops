import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    list = ec2.describe_instances()
    for i in list["Reservations"]:
        j = [ver_1["InstanceId"] for ver_1 in i["Instances"]]
        k = [ver_2["State"] for ver_2 in i["Instances"]]
        l = k[0]
        print("The Instance_id {0} is {1}".format(j,l["Name"]))
