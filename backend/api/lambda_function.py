import json
import boto3

# Create the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('kloudresume')

def lambda_handler(event, context):
    status_code = 200
    try:
        # Get the item from DynamoDB table
        response = table.get_item(
            Key={
                'id': 1,
            }
        )
        # Retrieve the value of count from DynamoDB table
        count = response['Item']['pageViews']

        # Increment Count by 1
        count = int(count) + 1

        # Retrieve value of id from DynamoDB table
        ID = response['Item']['id']

        # Update the value of Count in DynamoDB table 
        table.update_item(
            Key={
                'id': 1,
            },
            UpdateExpression='SET pageViews = :val1',
            ExpressionAttributeValues={
                ':val1': count
            }
        )
        # JSON body to be returned count to the frontend
        json_body = {'id': ID, 'pageViews': count}
        
    except Exception as e:
        status_code = 400
        json_body = {'error': str(e)}
    
    return {
        'statusCode': status_code,
        'body': json_body
    }