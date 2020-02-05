import os


class Config:
    NEWS_SOURCES_BASE_URL = "https://newsapi.org/v2/sources"
    NEWS_ARTICLES_BASE_URL = "https://newsapi.org/v2/everything"

    NEWS_CATEGORIES = [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
    ]
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {"development": DevConfig, "production": ProdConfig}
