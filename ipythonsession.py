# coding: utf-8
s3=session.resource('s3')
import boto3
session = boto3.Session(profile_name='automatepython')
s3 = session.resource('s3')
for bucket in s3.buckets.all():print(bucket)
get_ipython().run_line_magic('ls', '')
new_bucket = s3.create_bucket(Bucket='automatingawsarajesh-boto3')
for bucket in s3.buckets.all():print(bucket)
ec2_client=session.client('ec2')
get_ipython().run_line_magic('history', '')
