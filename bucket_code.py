import boto3

# Create an S3 resource
s3 = boto3.resource('s3')
# Create a bucket
mybucket = 'yanisbucket1160420241441'
s3.create_bucket(Bucket=mybucket)

# Upload file
with open('data/cities.csv', 'rb') as file:
    s3.Object(mybucket, 'cities.csv').put(Body=file)
    # Download file
    s3.Bucket(mybucket).download_file('cities.csv', 'cities_dl.csv')
    # Delete file
    s3 = boto3.resource('s3')
    s3.Object(mybucket, 'cities.csv').delete()

s3.Bucket(mybucket).delete()