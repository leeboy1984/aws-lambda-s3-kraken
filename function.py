from __future__ import print_function

import json
import urllib
import urllib2
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    
    # Start Kraken.io Config
    params = {
        'auth': {
            'api_key': 'KRAKEN_API_KEY',
            'api_secret': 'KRAKEN_SECRET_KEY'
        },
        'url': 'AWS_CDN_URL' + key,
        's3_store': {
            'key': 'AWS_IDENTITY_KEY', // Credentials from IAM
            'secret': 'AWS_IDENTITY_SECRET', // Credentials from IAM
            'bucket': 'BUCKET_NAME', // Your bucket name
            'path': key
        },
        'wait': True,
        'lossy': True
    }
    url = 'https://api.kraken.io/v1/url'
    # End Kraken.io Config
    
    try:
      #Start Kraken.io execution
      data = json.dumps(params)
      request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
      response = urllib2.urlopen(request)
      jsonRes = json.loads(str(response.read()))
     
      if (jsonRes['success']):
        print ('Success. Optimized image URL: ' + jsonRes['kraked_url'])
      else:
        print ('Fail. Error message: ' + jsonRes['message'])
      #End Kraken.io execution
    except Exception as e:
        print(e)
        print('Error optimizing object {} from bucket {}.'.format(key, bucket))
        raise e
