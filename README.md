# Leadplus News Project

## About
This is a Django project for Leadplus assignment which fetches news items from the [News API](https://newsapi.org) and stores them in a database. 

## Functionalities

1. A home page displays latest 20 news in database
    http://127.0.0.1:8000/
2. An API which returns the latest 100 from database
    http://127.0.0.1:8000/api/news_items
3. A command to fetch the latest 100 news under certain topic and save it to database
    ```bash
    ./manage.py fetch_news [TOPIC]
    ```
    For example, fetching top 100 news under topic `ai` would be:
    ```bash
    ./manage.py fetch_news ai
    ```

## How to setup

### 0. Before you start
This project is based on `python3`, make sure you have `python3` and `pip3` installed

### 1. clone reposetup virtual env

```bash
git clone git@github.com:JohnnyZhao/leadplus_news.git

```

### 2. setup virtual environment and install requirements

Change working directory and make an virtual environment called `.leadplus_news_env`:

```bash
cd leadplus_news

python3 -m venv .leadplus_news_env

source ./leadplus_news_env/bin/activate
```

Install dependencies:

```bash
pip3 install -r requirements.txt
```

### 3. config API key

Copy the sample config file under news/config.py.sample

```bash
cp news/config.py.sample news/config.py
```

Change the value of NEWS_API_KEY to a valid API Key for newsapi.org and save it

```python
#API key for newsapi.org, config it before fetch news
NEWS_API_KEY="VALID API KEY"

```

### 4. Migrate database and fetch news data

Migrate database:

```bash
./manage.py migrate
```

Fetch latest news data from newsapi.org via command `fetch_news`.
You need to specify a topic of news you want to fetch, for example `tech` news:

```
./manage.py fetch_news tech
```
which will fetch and save the latest 100 news and save it to database


### 5. Start Server

```bash
./manage.py runserver
```

Now you can visit http://127.0.0.1:8000/ in your preferred browser to check it.