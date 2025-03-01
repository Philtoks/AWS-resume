import json
import boto3

# Create the DynamoDB resource
table = boto3.client('dynamodb')

def lambda_handler(event, context):
    
    status_code = 200
    try:
        # Route key 
        
            # Get the item from table
            response = table.get_item(
                TableName= 'kloudresume',
                Key={
                    'id': {
                        'N': '1',
                    },
                }
            )
            # Retrieve the value of count from dynamoDB table
            count = response['Item']['pageViews']['N']

            # Increment Count by 1
            count = int(count) + 1

            # Retrieve value of id from table
            ID = response['Item']['id']['N']

            

            # Update the value of Count in dynamodB table 
            response = table.update_item(
                TableName= 'kloudresume',
                Key={
                    'id': {
                        'N': '1',
                    },
                },
                UpdateExpression='SET pageViews = :val1',
                ExpressionAttributeValues={
                    ':val1': {
                        'N': str(count),
                    }
                }
            )
            # JSON body to be returned to frontend
            json_body = {'id': ID, 'pageViews': count}
             
        
       
    except Exception as e:
        status_code = 400
        json_body = {'error': str(e)}
    
    return {
        'statusCode': status_code,
        'body': json.dumps(json_body)
    }   
