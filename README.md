# news-flash

> This project features a Flask application that consumes the News API to display different news articles from different sources

## Description

news-flash is a webapp that allows users to quickly access news highlights. It's powered by the wonderful News API from where it fetches categorized news articles from various news sources. news-flash is live at https://news-flashed.herokuapp.com/.

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

Install the project dependencies:

```
pip install -r requirements.txt
```

Setup the following environment variables:

```
export FLASK_APP=run.py
export NEWS_API_KEY=<GET_KEY_FROM_NEWS_API_ORG>
```

This is enough to get you started. You can now run the application using:

```
flask run
```

## Usage

On initialization, the application displays the `news-flash` homepage. Select any of the categories listed in the navbar. This should take you to a listing of news sources. From the plethora of sources available, select a preferred source to view the published articles. In the articles page, selecting an article should redirect you to the actual post.

## Built With...

- [Flask](http://flask.pocoo.org/)
- [Bootstrap](https://getbootstrap.com/)

## Contact

Nyota Mwangi - [@trucktar](https://twitter.com/trucktar/)
Project Link: https://github.com/trucktar/news-flash

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
