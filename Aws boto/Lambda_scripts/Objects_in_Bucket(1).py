import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('pichai')
    list = [object.key for object in bucket.objects.filter(Delimiter = '/')]
    print("The Objects in the Bucket are {}".format(list))
    
