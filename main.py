import os
import requests
import json
from typing import Final
from dotenv import load_dotenv


def readEnv():
    load_dotenv()
    NEWS_API_KEY: Final[str] = os.getenv('NEWS_API_KEY')
    TELEGRAM_API_KEY: Final[str] = os.getenv('TELEGRAM_API_KEY')
    return NEWS_API_KEY, TELEGRAM_API_KEY

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
    

def main():
    language = 'en'

    NEWS_API_KEY, TELEGRAM_API_KEY = readEnv()
    response = get_news(NEWS_API_KEY, language).json()

    #for initial build of sources, to get all sources keep languages in l:46 as empty str
    # save_sources_to_file(source_ids,language)


if __name__ == "__main__":
    main()