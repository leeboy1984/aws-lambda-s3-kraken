from __future__ import print_function

import json
import urllib
import urllib2
import boto3

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    
    # Start Kraken.io Config
    params = {
        'auth': {
            'api_key': 'AWS_IDENTITY_API_PUBLIC',
            'api_secret': 'AWS_IDENTITY_API_SECRET'
        },
        'url': 'AWS_CDN_URL' + key,
        's3_store': {
            'key': 'KRAKEN_PUBLIC_KEY',
            'secret': 'KRAKEN_SECRET_KEY',
            'bucket': 'BUCKET_NAME',
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
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e