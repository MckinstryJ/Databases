import boto3
import pandas as pd

s3 = boto3.resoure(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id="",
    aws_screat_access_key='mysecretkey'
)

# shows all buckets
for bucket in s3.buckets.all():
    print(bucket)

# saves file to bucket
goog = pd.DataFrame({'date': '2014-01-01',
                     'open': '10.2',
                     'high': '10.3',
                     'low': '10.2',
                     'close': '10.25'})
goog.to_csv('goog.csv')
s3.Bucket('stock-data').upload_file(Filename='goog.csv', Key='goog.csv')

# loading csv file directly from bucket
goog = s3.Bucket('stock-data').Object('goog.csv').get()
goog = pd.read_csv(goog['Body'], index_col=0)