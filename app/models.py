class NewsSource:
    def __init__(self, id, name, description):
        """ Class to define news source objects."""
        self.id = id
        self.name = name
        self.description = description


class NewsArticle:
    def __init__(self, title, description, url, image_url, published):
        """ Class to define news article objects."""
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.published = " at ".join(published.split("T")).rstrip("Z")
