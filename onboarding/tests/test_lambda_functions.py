import json
import pytest
from unittest.mock import patch, MagicMock
from lambda_functions.add_user_profile import add_user_profile
from lambda_functions.get_user_profile import get_user_profile


# Mock event and context objects to simulate Lambda invocation
mock_event = {
    'body': json.dumps({
        'Username': 'testuser',
        'FullName': 'Test User',
        'Bio': 'Bio goes here',
        'ProfilePictureURL': 'http://example.com/image.jpg'
    }),
    'queryStringParameters': {'UserID': 'testuser-uuid'}
}
mock_context = {}


@pytest.fixture
def dynamodb_mock():
    with patch('boto3.resource') as mock:
        # Mock the DynamoDB Table resource
        mock.return_value.Table.return_value = MagicMock(name='DynamoDBTable')
        yield mock.return_value.Table.return_value


@pytest.mark.unit
def test_add_user_profile(dynamodb_mock):
    # dynamodb_mock is now a mocked DynamoDB Table from the fixture
    dynamodb_mock.get_item.return_value = {'Item': {'UserID': 'testuser-uuid'}}
    dynamodb_mock.put_item.return_value = {}

    # Act
    response = add_user_profile(mock_event, mock_context)

    # Assert
    assert response['statusCode'] == 200
    dynamodb_mock.put_item.assert_called_once_with(Item=MagicMock())


@pytest.mark.unit
def test_get_user_profile(dynamodb_mock):
    # dynamodb_mock is now a mocked DynamoDB Table from the fixture
    dynamodb_mock.get_item.return_value = {
        'Item': {
            'UserID': 'testuser-uuid',
            'Username': 'testuser',
            'FullName': 'Test User',
            'Bio': 'Bio goes here',
            'ProfilePictureURL': 'http://example.com/image.jpg'
        }
    }

    # Act
    response = get_user_profile(mock_event, mock_context)

    # Assert
    assert response['statusCode'] == 200
    assert json.loads(response['body'])['UserID'] == 'testuser-uuid'
