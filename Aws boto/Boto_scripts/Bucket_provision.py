import boto3

s3 = boto3.client('s3')
ind = os.environ["NAME"]
create = s3.create_bucket(Bucket=ind) 
instance = ec2.create_instances(ImageId= id,
    	                            MinCount=1,
    	                            MaxCount=1,
    	                            InstanceType=type)
s3_list = s3.list_buckets()
buckets = [i['Name'] for i in s3_list['Buckets']]
print(buckets)