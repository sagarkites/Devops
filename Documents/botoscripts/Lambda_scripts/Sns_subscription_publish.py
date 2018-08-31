import boto3
def lambda_handler(event, context):
    sns = boto3.client('sns')
    topic =sns.create_topic(Name = "")
    print(topic)
    subscription = sns.subscribe(TopicArn = '',
                                 Protocol ='',
                                 Endpoint = '')
     publication =sns.public(TopicArn = '',
                             Message = '')
