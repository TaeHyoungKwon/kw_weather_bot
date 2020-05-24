import time
from os import environ
from selenium import webdriver

from constants import SECRET_BOARD_URL, weather_text


class WeatherBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

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
        print("완료")

    def submit_manual_weather_info(self):
        # 글쓰기 폼 클
        link = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/a')
        link.click()

        # 글쓰기 폼에 날씨정보 적기
        self.driver.find_element_by_css_selector("form")
        text_form = self.driver.find_element_by_name("text")
        text_form.send_keys(weather_text)


if __name__ == '__main__':
    weather_bot = WeatherBot()
    weather_bot.login()
    time.sleep(1)
    weather_bot.submit_manual_weather_info()