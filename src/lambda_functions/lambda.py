#serializeImageData
import json
import boto3
import base64

# S3 Client Setup
s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    """A function to serialize target data from S3"""

    key = event['s3_key']  
    bucket = event['s3_bucket'] \
    
    # Download the data from s3 to /tmp/image.png
  
    s3.download_file(bucket, key, '/tmp/image.png')
    
    with open("/tmp/image.png", "rb") as f:

        image_data = base64.b64encode(f.read())
        # image_data = base64.b64encode(f.read()).decode('utf-8')

    print("Event:", event.keys())

    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }  
        
		
		
################################################################################################
#classifyImageData
import json
import boto3
import base64


ENDPOINT = "image-classification-2025-08-17-13-50-49-557"


def lambda_handler(event, context):
    # Extract image data from the body
    body_data = event['body']
    image_data = body_data['image_data']
    
    # Decode the image data
    image = base64.b64decode(image_data)
    
    # Use boto3 SageMaker runtime client
    runtime = boto3.client('sagemaker-runtime')
    
    # Make a prediction
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image
    )
    
    # Get the inference result
    inferences = response['Body'].read().decode('utf-8')
    
    # Add inferences to the body data
    body_data["inferences"] = inferences
    
    return {
        'statusCode': 200,
        'body': body_data
    }


#########################################################################################
#filterInferences

import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    # Grab the inferences from the event
    body = event['body']
    
    
    if isinstance(body, str):
        body = json.loads(body)
    
    # Parse inferences
    inferences = json.loads(body['inferences']) if isinstance(body['inferences'], str) else body['inferences']
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(value > THRESHOLD for value in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }