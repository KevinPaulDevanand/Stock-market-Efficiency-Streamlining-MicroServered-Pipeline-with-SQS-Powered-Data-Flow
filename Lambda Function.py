import json
import boto3
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb',
    aws_access_key_id='',         
    aws_secret_access_key='',   
    region_name='eu-north-1')
    for record in event['Records']:
        
        
        message_body = record['body']
        message_body= message_body.replace("'", '"')
        json_body=json.loads(message_body)
        
        item = {
             
            'ID': {'S': str(json_body.get('ID', ''))},
            'timestamp': {'S': json_body.get('timestamp', '')},
            'price': {'N': str(json_body.get('price', '0'))}  
        }
         
            
            
        response=dynamodb.put_item(
                    TableName='Tesla_stock', 
                    Item=item
                )
            
         
        
    
        logger.info(f"Received SQS message: {message_body}")
