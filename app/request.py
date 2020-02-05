import json

import requests

from app import app

from .models import NewsArticle, NewsSource

api_key = app.config["NEWS_API_KEY"]


def process_news_sources(news_sources_list):
    """Creates news source objects.
    
    Args:
        news_sources_list (list): news sources fetched from the News API
    
    Returns:
        news_sources (list): news source objects
    """
    news_sources = []
    for news_source in news_sources_list:
        news_source_object = NewsSource(
            news_source["id"], news_source["name"], news_source["description"]
        )
        news_sources.append(news_source_object)

    return news_sources


def process_news_articles(news_articles_list):
    """Creates news article objects.
    
    Args:
        news_articles_list (list): news articles fetched from the News API
    
    Returns:
        news_articles (list): news article objects
    """
    news_articles = []
    for news_article in news_articles_list:
        news_article_object = NewsArticle(
            news_article["title"],
            news_article["description"],
            news_article["url"],
            news_article["urlToImage"],
            news_article["publishedAt"],
        )
        news_articles.append(news_article_object)

    return news_articles


def fetch_news_sources(category, language="en"):
    """Gets news sources from the /sources endpoint.
    
    Args:
        category (str): category of news. e.g., entertainment, business
        language (str): specific language of news. e.g., en, fr, gb 
    
    Returns:
        news_sources_results (list): processed news sources
    """
    news_sources_url = app.config["NEWS_SOURCES_BASE_URL"]
    # Query parameters
    payload = {"language": language, "apiKey": api_key}

    # Add category to query parameters
    if category:
        payload["category"] = category

    with requests.session() as session:
        news_sources_data = session.get(news_sources_url, params=payload)
        news_sources_response = news_sources_data.json()

        news_sources_results = None
        if news_sources_response["sources"]:
            news_sources_list = news_sources_response["sources"]
            news_sources_results = process_news_sources(news_sources_list)

    return news_sources_results


def fetch_news_articles(source):
    """Gets news articles from the /everything endpoint.
    
    Args:
        source (str): category of news. e.g., entertainment, business
    
    Returns:
        news_sources_results (list): processed news sources
    """
    news_articles_url = app.config["NEWS_ARTICLES_BASE_URL"]
    payload = {"sources": source, "apiKey": api_key}

    with requests.session() as session:
        news_articles_data = session.get(news_articles_url, params=payload)
        news_articles_response = news_articles_data.json()

        news_articles_results = None
        if news_articles_response["articles"]:
            news_articles_list = news_articles_response["articles"]
            news_articles_results = process_news_articles(news_articles_list)

    return news_articles_results
