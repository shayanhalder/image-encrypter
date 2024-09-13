# import boto3

# # s3 = boto3.resource('s3') # use for download
# s3 = boto3.client('s3') # use for upload

# # Define the file and bucket
# file_name = 'new-image.jpg'  # Path to your local file
# bucket_name = 'image-encrypter'  # S3 bucket name
# s3_file_name = 'shayan/new-image44.jpg'  # File name in S3
   
# # Upload the file
# response = s3.upload_file(file_name, bucket_name, s3_file_name)
# print(response)

# for bucket in s3.buckets.all():
#     print(bucket.name)

# # s3.Bucket('image-encrypter').download_file('Profile Picture.jpg', 'new-image.jpg')

    