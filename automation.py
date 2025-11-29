from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
browser = webdriver.Chrome()
sleep(2)
browser.get("https://youtube.com")
sleep(5)
element = browser.find_element("name","search_query")
search = "best indian food"
for char in search:
    element.send_keys(char)
    sleep(0.4)
element.send_keys(Keys.ENTER)
sleep(5)
first_short = browser.find_element("xpath",'//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div/div[1]/ytm-shorts-lockup-view-model-v2/ytm-shorts-lockup-view-model')
first_short.click()
sleep(30)
while True:
    next_btn =browser.find_element("xpath",'//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
    next_btn.click()
    sleep(0)
