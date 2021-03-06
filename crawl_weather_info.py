import requests
from bs4 import BeautifulSoup

from constants import NAVER_WEATHER_INFO_URL, USER_AGENT


def convert_text_to_soup(response):
    return BeautifulSoup(response.text, "html.parser")


def crawl_naver_weather_info():
    def _searched_weather(response):
        html = convert_text_to_soup(response)
        return html.find("div", {"class": "main_info"})

    response = requests.get(NAVER_WEATHER_INFO_URL, headers={"USER-AGENT": USER_AGENT})
    return _searched_weather(response)


def crawl_naver_weather_sub_info():
    def _searched_weather_sub_info(response):
        html = convert_text_to_soup(response)
        return html.find("div", {"class": "sub_info"})

    response = requests.get(NAVER_WEATHER_INFO_URL, headers={"USER-AGENT": USER_AGENT})
    return _searched_weather_sub_info(response)


def crawl_naver_humidity_info():
    def _searched_humidity(response):
            html = convert_text_to_soup(response)
            return html.find("div", {"class": "humidity"})

    response = requests.get(NAVER_WEATHER_INFO_URL, headers={"USER-AGENT": USER_AGENT})
    return _searched_humidity(response)
