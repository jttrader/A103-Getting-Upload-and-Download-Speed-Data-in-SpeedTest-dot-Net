from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

SPEED_TEST_URL = "https://www.speedtest.net/"
chrome_driver_path = r'F:\Python\Udemy\DevelopmentSelenium\chromedriver.exe'

class InternetSpeedBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path))
        self.up = 0
        self.down = 0

    #Opening speedtest.net and clicking the accept button, then clicking the GO button
    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        time.sleep(3)
        go_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        go_button.click()
        go_button = self.driver.find_element(By.CLASS_NAME, "start-button")
        go_button.click()

        # wait for 45 seconds to finish the test
        time.sleep(45)

        # once test has been finished the URL will change and get the current URL to store it, as after some
        # seconds after the test the URL goes back to default speedtest.net
        # collect the Download speed and Upload speed by XPATH

        current_result_url = self.driver.current_url
        self.driver.get(current_result_url)
        upload_result = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div/div[2]/span").text
        download_result = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div[2]/span").text
        print(f"Your download speed is {download_result} MBit/s and your upload speed is {upload_result} MBit/s")

speed_test = InternetSpeedBot(chrome_driver_path)
speed_test.get_internet_speed()



