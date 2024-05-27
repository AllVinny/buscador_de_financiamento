from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Driver:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service)

    def open(self, url):
        self.browser.get(url)

    def wait_located(self, by, element, time=5):
        return WebDriverWait(self.browser, time).until(
            EC.presence_of_element_located((by, element))
        )
