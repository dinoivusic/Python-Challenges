from selenium import webdriver
url = 'https://www.seleniumeasy.com/test/'

chrome = webdriver.Chrome('./chromedriver')
chrome.maximize_window()
chrome.get(url)

show_message = chrome.find_element_by_class_name('btn-default')
user_message = chrome.find_element_by_id('user-message')


user_message.clear()
user_message.send_keys('I AM AMAZING')

show_message.click()
output = chrome.find_element_by_id('display')

assert 'I AM AMAZING' in output

chrome.close()


