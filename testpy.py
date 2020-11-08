from selenium import webdriver
import sched, time, os, urllib.parse, re
from time import sleep
import listoffunctions
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys
# set variables
driver = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
driver.get("https://www.oddsmonkey.com/oddsmonkeyLogin.aspx?returnurl=%2f")
sleep(5)
driver.execute_script('window.open("https://www.sportingindex.com/fixed-odds","_blank");')
driver.switch_to.window(driver.window_handles[1])
driver.get("https://www.google.com")
sleep(5)
driver.execute_script('window.open("https://www.yahoo.com","_blank");')
sleep(5)
driver.switch_to.window(driver.window_handles[2])
driver.get("https://www.clifton-media.co.uk")

sleep(3)
driver.get("https://www.sky.co.uk")
sleep(3)
driver.switch_to.window(driver.window_handles[1])
sleep(3)
driver.close()
driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.get("https://www.htc.com")
