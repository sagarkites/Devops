import boto3
ec2 = boto3.client('ec2')
allocation = ec2.allocate_address(Domain = 'vpc')
Response = ec2.associate_address(AllocationId = 'eipalloc-03da8bd6aeeb76bd2', InstanceId = 'i-0958af30b0eddd67c')
print(Response)
