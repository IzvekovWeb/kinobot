import requests

from random import random

base_url = "https://api.kinopoisk.dev"
API_TOKEN = "cc82e1f619f93cde16671e00dacdc3e8"


def get_movies():
    page = int(random() * 1000)
    url = f"{base_url}movies/all/page/{page}/token/{API_TOKEN}"
    print(url)
    response = requests.get(url)
    print(response.text)


if __name__ == '__main__':
    get_movies()
