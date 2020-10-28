import boto3
import pandas_redshift as pr  # uses psycopg2 to connect to redshift and boto3 for s3
import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker

'''
    Connection to S3, Redshift
'''

# Connection to S3 via boto
s3 = boto3.resoure(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id="",
    aws_screat_access_key='mysecretkey'
)

# Connection to S3 via pandas_redshift
pr.connect_to_s3(aws_access_key_id= '',
                 aws_secret_access_key= '',
                 bucket= '',
                 subdirectory= '')

# Connection to Redshift via pandas_redshift
pr.connect_to_redshift(dbname= '',
                       host= '',
                       port= '',
                       user= '',
                       password= '')

# Connection to Redshift via psycopg2
conn = psycopg2.connect("dbname={} host={} port={} user={} password={}")

# Connection to Redshift via sqlalchemy -> psycopg2
conn_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)
engine = sqlalchemy.create_engine(conn_string)
session = sessionmaker()
sessioin.configure(bind=engine)
s = session()

# Shows all buckets
for bucket in s3.buckets.all():
    print(bucket)

'''
    Saving to S3, Redshift
'''

# Saving DataFrame to file then to s3 bucket
goog = pd.DataFrame({'date': '2014-01-01',
                     'open': '10.2',
                     'high': '10.3',
                     'low': '10.2',
                     'close': '10.25'})
goog.to_csv('goog.csv')
s3.Bucket('stock-data').upload_file(Filename='goog.csv', Key='goog.csv')

# Saving DataFrame to Redshift (saves to S3 then transfers file to Redshift) via pandas_to_redshift
pr.pandas_to_redshift(data_frame= goog,
                      redshift_table_name= 'PTC.GOOG')

# Saving DataFrame to Redshift via psycopg2
cur = conn.cursor()
cur.execute("INSERT INTO PTC.GOOG;")
cur.close()
conn.close()

# Loading csv file directly from bucket
goog = s3.Bucket('stock-data').Object('goog.csv').get()
goog = pd.read_csv(goog['Body'], index_col=0)

# Loading table from Redshift
goog = pr.redshift_to_pandas('SELECT * FROM PTC.GOOG')
