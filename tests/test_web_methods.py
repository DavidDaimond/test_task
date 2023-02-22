import pytest

import requests as req
import json
import re
import time

from selenium.webdriver.common.by import By

from config import WebPage, API
from utils import run_driver, MainPage


@pytest.fixture(scope='module', name='driver')
def start_driver():
    driver = run_driver(True)

    yield driver

    driver.close()


@pytest.fixture(scope='module', name='main_page')
def get_main_page(driver):
    driver.get(WebPage.url)

    endpoints_element = driver.find_element(By.CLASS_NAME, WebPage.endpoints_block_class)
    response_element = driver.find_element(By.CLASS_NAME, WebPage.response_block_class)
    request_element = driver.find_element(By.CLASS_NAME, WebPage.request_block_class)

    _endpoints_blocks = endpoints_element.find_elements(By.TAG_NAME, WebPage.endpoint_tag)

    endpoints_blocks = {re.sub("[<>]", "", re.sub("[ \-]+", "_", block.text)) + "_" +
                        block.get_attribute('data-http').upper(): block for block in _endpoints_blocks}

    main_page = MainPage(endpoints_element=endpoints_element,
                         response_element=response_element,
                         request_element=request_element,
                         endpoints_blocks=endpoints_blocks)
    yield main_page


@pytest.mark.parametrize('block_name', list(API.methods.keys()))
def test_web_to_api(driver, main_page, block_name):
    block = main_page.endpoints_blocks[block_name]
    block.click()
    time.sleep(.45)
    method = block.get_attribute('data-http')
    url = main_page.request_element.find_element(By.TAG_NAME, "a").get_attribute('href')

    data = None
    output_request = main_page.request_element.find_element(By.TAG_NAME, 'pre')
    if not output_request.get_attribute('hidden'):
        data = json.loads(output_request.text)

    resp = req.request(method, url) if data is None else req.request(method, url, data=data)

    response_code = int(main_page.response_element.find_element(By.CLASS_NAME, 'response-code').text)
    assert response_code == resp.status_code
    if method == 'delete':  # delete delete because it has not
        return

    response_message = json.loads(main_page.response_element.find_element(By.TAG_NAME, 'pre').text)
    response = resp.json()
    for time_data in ("updatedAt", "createdAt"):  # because this params will not be same
        response_message[time_data] = None
        response[time_data] = None
    assert response_message == response
