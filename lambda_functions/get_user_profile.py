import json
import boto3

# Initialize a boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'cp-onboarding-user-profiles'
table = dynamodb.Table(table_name)


def get_user_profile(event, context):
    # Extract the user ID from the request parameters
    user_id = event['queryStringParameters']['UserID']

    try:
        # Attempt to retrieve the user data from DynamoDB
        response = table.get_item(Key={'UserID': user_id})

        # Check if the user profile exists
        if 'Item' in response:
            user_profile = response['Item']
            return {
                'statusCode': 200,
                'body': json.dumps(user_profile)
            }
        else:
            # User profile not found
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }
