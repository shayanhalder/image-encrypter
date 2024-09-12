import requests

# URL of the image served via CloudFront (replace with your CloudFront domain and file path)
cloudfront_url = 'https://d1s4n8hdqe9v3.cloudfront.net/new-image.jpg'

# Make a GET request to fetch the image
response = requests.get(cloudfront_url)

# print(response)
# print(response.text)
# print(response.status_code)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the image data (binary format)
    image_data = response.content
    
    # Optionally, save the image to a local file
    with open('downloaded_image.jpg', 'wb') as file:
        file.write(image_data)
    
    print("Image successfully downloaded and saved!")
else:
    print(f"Failed to retrieve the image. Status code: {response.status_code}")



# {
# 	"Version": "2008-10-17",
# 	"Id": "PolicyForCloudFrontPrivateContent",
# 	"Statement": [
# 		{
# 			"Sid": "AllowCloudFrontServicePrincipal",
# 			"Effect": "Allow",
# 			"Principal": {
# 				"Service": "cloudfront.amazonaws.com"
# 			},
# 			"Action": "s3:GetObject",
# 			"Resource": "arn:aws:s3:::image-encrypter/*",
# 			"Condition": {
# 				"StringEquals": {
# 					"AWS:SourceArn": "arn:aws:cloudfront::234146233304:distribution/E2CNTGHFOGKISJ"
# 				}
# 			}
# 		}
# 	]
# }