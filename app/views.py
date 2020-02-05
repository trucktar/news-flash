import random

from flask import redirect, render_template, url_for

from app import app

from .request import fetch_news_articles, fetch_news_sources

categories = app.config["NEWS_CATEGORIES"]


@app.route("/")
@app.route("/news-sources/<category>")
def news_sources(category=None):
    """  """
    title = "News Sources | News Flash"

    if category and category in categories:
        sources = fetch_news_sources(category)
        return render_template(
            "news-sources.html", title=title, categories=categories, sources=sources
        )
    else:
        sources = None
        return render_template(
            "news-sources.html", title=title, categories=categories, sources=sources
        )


@app.route("/news-articles/<source>")
def news_articles(source):
    title = "News Articles | News Flash"

    articles = fetch_news_articles(source)
    return render_template(
        "news-articles.html", title=title, categories=categories, articles=articles
    )