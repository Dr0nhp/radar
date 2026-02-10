import os
import json
import news
import bot
from typing import Final
from dotenv import load_dotenv


def readEnv():
    load_dotenv()
    NEWS_API_KEY: Final[str] = os.getenv('NEWS_API_KEY')
    TELEGRAM_API_KEY: Final[str] = os.getenv('TELEGRAM_API_KEY')
    return NEWS_API_KEY, TELEGRAM_API_KEY

def main():
    language = 'en'
    NEWS_API_KEY, TELEGRAM_API_KEY = readEnv()
    news_response = news.get_news(NEWS_API_KEY, language).json()

if __name__ == "__main__":
    main()