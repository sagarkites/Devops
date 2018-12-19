import boto3
ec2 = boto3.resource('ec2')
for i in ec2.instances.all():
	tg = [i.id for t in i.tags if t['Value'] == 'sagar_scott']
	for k in tg:
	     instance = ec2.Instance(k).start()   
	     print(instance)