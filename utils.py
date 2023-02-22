from dataclasses import dataclass

from selenium import webdriver

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import System


@dataclass
class MainPage:
    endpoints_blocks: dict[str, WebElement]
    endpoints_element: WebElement
    response_element: WebElement
    request_element: WebElement


def run_driver(download=False):
    if download:
        webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return webdriver.Chrome(service=Service(System.webdriver_path))

