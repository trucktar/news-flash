# news-flash

> This project features a Flask application that consumes the News API to display different news articles from different sources

## Description

`news-flash` is a webapp that allows users to quickly access news highlights. It's powered by the wonderful News API from where it fetches categorized news articles from various news sources.

`news-flash` is live at https://news-flashed.herokuapp.com/.

## Getting Started

These instructions will get you a copy of this project up and running on your local machine for developmental and testing purposes.

Clone the repo from GitHub:

```
git clone https://github.com/trucktar/news-flash.git
```

Navigate to the root folder:

```
cd news-flash
```

Create and activate a virtual environment:

```
python3 -m venv virtual
source virtual/bin/activate
```

Install the project's dependencies:

```
pip install -r requirements.txt
```

Setup the following environment variables:

```
export NEWS_API_KEY=<YOUR_NEWS_API_KEY>
```

To launch the app, run `python run.py`. Alternatively, set the `FLASK_APP` environment variable with the value `run`, and run the app using the command `flask run`. This will launch the Flask server on `http://127.0.0.1:5000/`.

## Usage

On initialization, the application displays the `news-flash` homepage. Select any of the categories listed in the navbar. This should take you to a listing of news sources.

![Landing](https://github.com/trucktar/news-flash/blob/master/app/static/images/landing.png)

From the plethora of sources available, select a preferred source to view the published articles.

![Sources](https://github.com/trucktar/news-flash/blob/master/app/static/images/sources.png)

In the articles page, selecting an article should redirect you to the actual post.

![Articles](https://github.com/trucktar/news-flash/blob/master/app/static/images/articles.png)

## Built With...

- [Flask](http://flask.pocoo.org/)
- [Bootstrap](https://getbootstrap.com/)

## Built By...

&copy; 2020 - [Nyota Mwangi](https://twitter.com/trucktar/)

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
