# aws-lambda-s3-kraken
Function for optimizing files when are uploaded to an s3 bucket

## PRE-REQUISITES
Amazon AWS account (With an S3 bucket and Cloudfront configured to use the same or a different bucket)
Kraken.io account. If you don't have an account you can register using this link --> https://kraken.io/?ref=23bcad74f2a8

## CONFIGURATION
1.- Create a Lambda function in order to watch an S3 bucket in your account and be triggered when an object is created. Add image type extensions as suffix in order to filter just image objects
2.- Paste python code in your function
3.- Modify the code and put your variable values
4.- Use the attached event example in your test event
5.- Modify the code and put your variable values

## Execution
This Lambda function will be triggered every time an object is uploaded to the S3
