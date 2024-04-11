import json
import uuid
import boto3

# Initialize a boto3 DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'cp-onboarding-user-profiles'
table = dynamodb.Table(table_name)


def add_user_profile(event, context):
    try:
        user_data = json.loads(event.get('body', ''))
    except json.JSONDecodeError:
        return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid JSON format in request body'})}

    # Generate a unique user ID
    user_id = str(uuid.uuid4())
    if 'UserID' in table.get_item(Key={'UserID': user_id}).get('Item', {}):
        return {'statusCode': 500, 'body': json.dumps({'error': 'User ID already exists'})}

    # Prepare the item to insert
    item = {
        'UserID': user_id,
        'Username': user_data.get('Username', ''),
        'FullName': user_data.get('FullName', ''),
        'Bio': user_data.get('Bio', ''),
        'ProfilePictureURL': user_data.get('ProfilePictureURL', '')
    }

    # Insert the item into DynamoDB
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'User profile added',
                'user_profile': item
            })
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not insert the user profile into the database'})
        }
