import boto3
ec2 = boto3.client('ec2')
sns = boto3.client('sns')
list = ec2.describe_instances()
for i in list["Reservations"]:
    j = [instance["InstanceId"] for instance in i["Instances"]]
    k = [response["State"] for response in i["Instances"]]
    l = k[0]
    if l["Name"] == "running":
        shutdown = (ec2.stop_instances(InstanceIds=j))
        res = "The Running Instances {} are shutdowned".format(j)
        print(res)
        sub = sns.subscribe(TopicArn = 'arn:aws:sns:us-east-1:432790052604:instances',
	                Protocol = 'email',
	                Endpoint = 'vidyasagarchintaluri@gmail.com')
        pub = sns.publish(Message = 'res', TopicArn ='arn:aws:sns:us-east-1:432790052604:instances' )
