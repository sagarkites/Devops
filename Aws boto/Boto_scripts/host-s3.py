import boto3
# Hosting to s3
s3 = boto3.client('s3')
web = {'ErrorDocument':{'Key':'error.html'},'IndexDocument':{'Suffix':'index.html'}}
upload_file = s3.put_bucket_website(Bucket='sagarscott',
                                      WebsiteConfiguration=web)
print(upload_file)
get = s3.get_bucket_website(Bucket='sagarscott')
File1 = s3.upload_file('/Users/pavanscott/index.html','sagarscott','index.html')
File2 = s3.upload_file('/Users/pavanscott/index.html','sagarscott','error.html')
print(File1)
print(File2)
