from decimal import Decimal

def parse_data(**kwargs):
    # get the task instance
    task_instance = kwargs['ti']
    # get the XCom value
    raw_data = task_instance.xcom_pull(task_ids='extract_top_25')
    
    
    # Parse the JSON response
    top_25 = raw_data
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
    return res