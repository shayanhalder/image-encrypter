import boto3

s3 = boto3.resource('s3')
# s3 = boto3.client('s3')

# Define the file and bucket
file_name = 'Profile Picture.jpg'  # Path to your local file
bucket_name = 'image-encrypter'  # S3 bucket name
s3_file_name = 'shayan/new-image.jpg'  # File name in S3

# Upload the file
# s3.upload_file(file_name, bucket_name, s3_file_name)


# # for bucket in s3.buckets.all():
# #     print(bucket.name)

s3.Bucket('image-encrypter').download_file('Profile Picture.jpg', 'new-image.jpg')

    