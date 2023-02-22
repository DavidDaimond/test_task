from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import System


def run_driver(download=False):
    if download:
        webdriver.Chrome(service=Service(ChromeDriverManager.install()))
    return webdriver.Chrome(service=Service(System.webdriver_path))

