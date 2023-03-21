# Leadplus News Project

## About

This is a Django project for the Leadplus assignment, which fetches news items from the [News API](https://newsapi.org) and stores them in a database. The project provides a home page that displays the latest 20 news items, an API that returns the latest 100 news items, and a command to fetch the latest 100 news items under a certain topic and save them to the database.

## Functionalities

1. A home page displays the latest 20 news items: http://127.0.0.1:8000/
2. An API which returns the latest 100 news items: http://127.0.0.1:8000/api/news_items
3. A command to fetch the latest 100 news items under a certain topic and save them to the database:
    ```bash
    ./manage.py fetch_news [TOPIC]
    ```
    For example, fetching the top 100 news items under the topic `ai` would be:
    ```bash
    ./manage.py fetch_news ai
    ```

## How to set up

### Prerequisites

This project is based on `Python 3.10.9`. Please ensure that you have at least `Python 3.10.9+` and `pip3` installed. You can find more information about the latest Python version here: https://www.python.org/downloads/

### Step-by-step instructions

1. Clone the repository:

    ```bash
    git clone git@github.com:JohnnyZhao/leadplus_news.git
    ```

2. Setup a virtual environment and install requirements:

    Change to the project directory:

    ```bash
    cd leadplus_news
    ```

    Create a virtual environment called `.leadplus_news_env`:

    ```bash
    python3 -m venv .leadplus_news_env
    ```

    Activate the virtual environment:

    ```bash
    source ./.leadplus_news_env/bin/activate
    ```

    Install dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Configuring the [News API](https://newsapi.org) key:

    Copy the sample config file under the `news` folder `news/config.py.sample`:

    ```bash
    cp news/config.py.sample news/config.py
    ```

    Change the value of `NEWS_API_KEY` in `news/config.py` to a valid API Key from newsapi.org and save it:

    ```python
    # API key for News API, config it before fetching news
    NEWS_API_KEY="REPLACE THIS WITH A VALID API KEY"
    ```

4. Migrate the database and populate news items:

    Migrate the database:

    ```bash
    ./manage.py migrate
    ```

    Fetch the latest 100 news items from [News API](https://newsapi.org) via the `fetch_news` command. You need to specify a topic of news you want to fetch, for example, `tech` news:

    ```
    ./manage.py fetch_news tech
    ```

    This will fetch the latest 100 news items and save them to the database.

5. Start the server:

    ```bash
    ./manage.py runserver
    ```

    You can now visit http://127.0.0.1:8000/ in your preferred browser to check it.

6. [Optional] Create a superuser and access Django admin site:

    Create a superuser via:

    ```bash
    ./manage.py createsuperuser
    ```

    You can now log in to http://127.0.0.1:8000/admin to check and manage news records in the database.
