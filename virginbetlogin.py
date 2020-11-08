from selenium import webdriver
import sched, time, os, urllib.parse, re
from time import sleep
import listoffunctions
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
refresh_time_in_seconds = 20
betamount = 1
logintomarathonbet = 1
driver.get("https://www.google.com")
sleep(3)

if logintomarathonbet:

    driver.execute_script('window.open("https://www.marathonbet.co.uk/en/","_blank");')
    driver.switch_to.window(driver.window_handles[-1])
    sleep(3)

    driver.find_element_by_xpath("//input[@data-name='login']").send_keys('markiepollak')
    driver.find_element_by_xpath("//input[@data-name='login_password']").send_keys('Marathonbet!11')
    sleep(3)
    # driver.find_elements_by_name("auth-form__input").send_keys('markiepollak')
    driver.find_element_by_xpath('//div[@class="input-group-prepend"]//button').click()
