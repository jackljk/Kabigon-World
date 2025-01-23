import json
import boto3
from decimal import Decimal
from datetime import datetime, timezone
import requests
# Fetch data from Jikan API
def get_top_data():
    url = "https://api.jikan.moe/v4/top/anime"
    try:
        # Make a GET request to the Jikan API
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the JSON response
        top_25 = response.json()
        res = []
        for data in top_25['data'][0:25]:  # Get only the top 25 entries
            item = {
                'mal_id': data['mal_id'],
                'title': data['title'],
                'url': data['url'],
                'image_url': data['images']['webp']['image_url'],
                'title_english': data.get('title_english'),  # Use .get() to handle missing keys
                'title_japanese': data.get('title_japanese'),
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
        print(res)
        return res
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching data from Jikan API: {str(e)}")

# Generate unique ID
def get_next_id(dynamodb):
    counter_table = dynamodb.Table('atomic-counter')
    response = counter_table.update_item(
        Key={'id_counter': 'dashboard-top-25'},
        UpdateExpression='ADD last_used_id :increment',
        ExpressionAttributeValues={':increment': 1},
        ReturnValues='UPDATED_NEW'
    )
    return int(response['Attributes']['last_used_id'])

# Generate timestamp
def get_timestamp():
    timestamp = datetime.now(timezone.utc).isoformat(timespec='seconds').replace("+00:00", "Z")
    return timestamp

# Add data to DynamoDB
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
        response = table.put_item(Item=item)
        return response, item
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Failed to write to DynamoDB: {str(e)}"
        }

# Lambda handler
def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    # Use asyncio to run the async function
    result = add_to_db(dynamodb)
    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully added to db!!')
    }
