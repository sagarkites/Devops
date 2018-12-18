import boto3
# Enable or Disble Monitoring
ec2 = boto3.client('ec2')
Cloud_watch_on = ec2.monitor_instances(InstanceIds = ['i-0958af30b0eddd67c'])
Cloud_watch_off = ec2.unmonitor_instances(InstanceIds = ['i-0958af30b0eddd67c'])
print(Cloud_watch_off)
