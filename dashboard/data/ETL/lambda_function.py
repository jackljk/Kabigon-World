import json
import boto3
from decimal import Decimal
from jikanpy import AioJikan
from datetime import datetime, timezone

def get_top_data():
    top_25 = Jikan.jikan.top(type='anime', page=1)['data'][0:25]
    res = []
    for data in top_25:
        item = {
            'mal_id': data['mal_id'],
            'title': data['title'],
            'url': data['url'],
            'image_url': data['images']['webp']['image_url'],
            'title_english': data['title_english'],
            'title_japanese': data['title_japanese'],
            'licensors': {
                'names': [x['name'] for x in data['licensors']],
                'urls':  [x['url'] for x in data['licensors']]
            },
            'studios': {
                'names': [x['name'] for x in data['studios']],
                'urls': [x['url'] for x in data['studios']]
            },
            'genres': [x['name'] for x in data['genres']],
            'statistics': {
                'rank': Decimal(str(data['rank'])),
                'score': Decimal(str(data['score'])),
                'members': Decimal(str(data['members'])),
                'favorites': Decimal(str(data['favorites'])),
                'scored_by': Decimal(str(data['scored_by'])),
                'popularity': Decimal(str(data['popularity']))
            }
        }
        res.append(item)
    return res
def get_next_id(dynamodb):
    counter_table = dynamodb.Table('atomic-counter')
    # Update the counter atomically
    response = counter_table.update_item(
        Key={'id_counter': 'dashboard-top-25'},  # Identifier for the counter item
        UpdateExpression='ADD last_used_id :increment',
        ExpressionAttributeValues={':increment': 1},  # Increment value
        ReturnValues='UPDATED_NEW'  # Return the updated value
    )
    # Return the new unique ID
    return int(response['Attributes']['last_used_id'])

def get_timestamp():
    # Generate current timestamp in ISO 8601 format with UTC timezone and explicit Z
    timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z")
    return timestamp

def add_to_db(dynamodb):
    try:
        # Fetch data from Jikan API
        data = get_top_data()
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Failed to fetch data from Jikan API: {str(e)}"
        }

    try:
        table = dynamodb.Table('anime-dashboard-top-25')
        item = {
            'id': get_next_id(dynamodb),
            'timestamp': get_timestamp(),
            'data': data,
        }
        # Insert data into DynamoDB
        response = table.put_item(Item=item)
        return response, item
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Failed to write to DynamoDB: {str(e)}"
        }
    
    return response, item

def lambda_handler(event, context):
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    add_to_db(dynamodb)


    return {
        'statusCode': 200,
        'body': json.dumps('Successfully added to db!')
    }
