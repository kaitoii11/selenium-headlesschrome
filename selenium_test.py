#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location='/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome'
options.add_argument('--headless')
# need to add path to chromedriver
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.google.co.jp/')

input = driver.find_element_by_name('q')
input.send_keys('Python')
input_element.send_keys(Keys.RETURN)

driver.save_screenshot('result.png')

driver.quit()

