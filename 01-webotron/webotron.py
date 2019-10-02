import boto3
import click
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "yahelautomation deplpys websites to AWS"
    pass

@cli.command('list_buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list_buckets_objects')
@click.argument ('bucket')
def list_buckets_objects(bucket):
    "List Objects in an s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

@cli.command('setup_bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and confugre s3 bucket"
    session.region_name
    s3_bucket = s3.create_bucket(
    Bucket=bucket, CreateBucketConfiguration={'LocationConstraint': session.region_name}
    )
#    s3_bucket = None
#    try:
#    except ClientError as e:
#        if e.response['Error']['Code'] == "BucketAlreadyOwnedByYou":
            #s3_bucket = s3.Bucket (bucket)
#            print ("BucketAlreadyOwnedByYou, create other name bucket")
#        else:
#            raise e

#    new_bucket.upload_file('index.html', 'index.html', ExtraArgs={'ContentType': 'text/html'} )

    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[{
        "Sid":"PublicReadGetObject",
            "Effect":"Allow",
          "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::%s/*"
          ]
        }
      ]
    }
    """ % s3_bucket.name
    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)
    ws = s3_bucket.Website()

    ws.put(WebsiteConfiguration={
        'ErrorDocument': {
            'Key': 'error.html'
        },

        'IndexDocument': {
            'Suffix': 'index.html'
        }})
    return
#    url="https://%s.s3-website.us-east-2.amazonaws.com" % new_bucket.name
#    url

if __name__ == '__main__':
    cli()
