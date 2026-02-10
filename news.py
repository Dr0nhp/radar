import requests

def get_news(api_key,language):
    API_ENDPOINT: Final[str] = 'https://newsapi.org/v2/top-headlines/sources'

    headers = {
        'Authorization': api_key
    }

    params = {
        'language': language
    }

    response = requests.get(API_ENDPOINT, params=params, headers=headers)
    return response

def save_sources_to_file(source_ids,language, filename="sources.json"):
    source_ids = [source['id'] for source in response['sources']]

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {}

    data[language] = {
        "sources": source_ids
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

