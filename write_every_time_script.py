import time
from datetime import datetime, timedelta
from os import environ
from selenium import webdriver

from constants import (
    SECRET_BOARD_URL,
    weather_text,
    WEATHER_AUTO_TEXT,
    WEEK_DAY,
    DATE_FORMAT,
    DATETIME_FORMAT,
    OVER_30_DEGREE,
    CLOTHES_TEXT,
)
from crawl_weather_info import crawl_naver_weather_info
from helpers import choose_clothes


class WeatherBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(chrome_options=options)

    @staticmethod
    def reform_weather_info():
        utc_now = datetime.utcnow()
        local_now = utc_now + timedelta(hours=9)
        weather_info_html = crawl_naver_weather_info()

        rainfall = weather_info_html.find("span", {"class": "rainfall"})
        uv = weather_info_html.find("span", {"class": "indicator"})

        detail_info = ""
        if not (uv or rainfall):
            detail_info = "자외선, 강수 정보가 제공되지 않고 있습니다."
        else:
            if not rainfall:
                detail_info = uv.text
            if not uv:
                detail_info = rainfall.text

        min_temperature = weather_info_html.find("span", {"class": "min"}).text
        max_temperature = weather_info_html.find("span", {"class": "max"}).text

        int_min_temperature = int(min_temperature.replace("˚", ""))
        int_max_temperature = int(max_temperature.replace("˚", ""))

        if int_max_temperature > 30:
            clothes_message = OVER_30_DEGREE
        if int_min_temperature < 0:
            clothes_message = OVER_30_DEGREE
        else:
            clothes_message = CLOTHES_TEXT.format(
                clothes_first=choose_clothes(int_min_temperature), clothes_seconds=choose_clothes(int_max_temperature)
            )

        weather_info = {
            "today_date": local_now.strftime(DATE_FORMAT),
            "week_day": WEEK_DAY[local_now.weekday()],
            "today_datetime": local_now.strftime(DATETIME_FORMAT),
            "today_temp": weather_info_html.find("span", {"class": "todaytemp"}).text + " 도",
            "cast_txt": weather_info_html.find("p", {"class": "cast_txt"}).text,
            "min_temperature": min_temperature,
            "max_temperature": max_temperature,
            "sensible": weather_info_html.find("span", {"class": "sensible"}).text,
            "detail_info": detail_info,
            "clothes_message": clothes_message,
        }
        return WEATHER_AUTO_TEXT.format(**weather_info)

    def _submit_weather_info(self, contents):
        self.driver.find_element_by_css_selector("form")
        text_form = self.driver.find_element_by_name("text")
        text_form.send_keys(contents)
        text_form.submit()

    def _click_form(self):
        link = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/a")
        link.click()

    def login(self):
        self.driver.get(SECRET_BOARD_URL)
        time.sleep(1)

        # Get Login Form
        self.driver.find_element_by_css_selector("form")

        # Input ID
        account_info = self.driver.find_element_by_name("userid")
        account_info.send_keys(environ["EVERY_TIME_ID"])

        # Input PW
        account_info = self.driver.find_element_by_name("password")
        account_info.send_keys(environ["EVERY_TIME_PW"])
        account_info.submit()

    def submit_manual_weather_info(self):
        self._click_form()
        self._submit_weather_info(contents=weather_text)

    def submit_auto_weather_info(self):
        self._click_form()
        print(self.reform_weather_info())
        self._submit_weather_info(contents=self.reform_weather_info())
        print("완료스!")


if __name__ == "__main__":
    weather_bot = WeatherBot()
    weather_bot.login()
    time.sleep(1)
    weather_bot.submit_auto_weather_info()
