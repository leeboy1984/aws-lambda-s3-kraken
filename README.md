# aws-lambda-s3-kraken
Function for optimizing files when are uploaded to an s3 bucket

### PRE-REQUISITES
Amazon AWS account (With an S3 bucket and Cloudfront configured to use the same or a different bucket)
Kraken.io account. <br/>
If you don't have an account you can register using this link --> https://kraken.io/?ref=23bcad74f2a8

### CONFIGURATION
1.- Create a Lambda function in order to watch an S3 bucket in your account and be triggered when an object is created. Add image type extensions as suffix in order to filter just image objects<br/>
2.- Paste python code in your function<br/>
3.- Modify the code and put your variable values<br/>
4.- Use the attached event example in your test event<br/>
5.- Modify the code and put your variable values<br/>

### Execution
This Lambda function will be triggered every time an object is uploaded to the S3<br/>

### Considerations
At this momment Kraken.io with S3 always overwrite the object even the object is already optimized. An update in their API is pending in order to avoid loops; if finally Kraken.io does not change its way of working, I will modify the function for avoiding loops
