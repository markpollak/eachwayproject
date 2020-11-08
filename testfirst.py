from selenium import webdriver
import sched, time, os, urllib.parse, re
from time import sleep
import listoffunctions
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys
# set variables
driver = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
refresh_time_in_seconds = 15
betamount = 0.5
eachway = 1
numberofplaces = 4

logintosportingindex = 1
logintooddsmonkey = 1
oddsmonkeyusernameenviron = os.environ.get("oddsmonkeyusername")
oddsmonkeypasswordenviron = os.environ.get("oddsmonkeypassword")

# log into oddsmonkey
if logintooddsmonkey:
    listoffunctions.logintooddsmonkey(driver,oddsmonkeyusernameenviron,oddsmonkeypasswordenviron)


sleep(3)
dateofracecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td')
dateofrace = dateofracecell.text.lower()
racetime = dateofrace[-5:]
# print(dateofrace)
racevenuecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[8]')
racevenue = racevenuecell.text.lower().strip()
sizestring = len(racevenue)
# Slice string to remove last 3 characters from string
racevenue = racevenue[:sizestring - 5].strip()
# print(racevenue)
horsenamecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[9]')
horsename = horsenamecell.text.title()

horseoddscell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[13]')
horseodds = horseoddscell.text

bookmakerlinkcell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[10]//a')
bookmakerlink = bookmakerlinkcell.get_attribute('href')
bookmakerlink = listoffunctions.parsetheexchangelinks(bookmakerlink)
bookmaker = bookmakerlink

winexchangelinkcell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[14]//a')
winexchangelink = winexchangelinkcell.get_attribute('href')
winexchangelink = listoffunctions.parsetheexchangelinks(winexchangelink)


placeexchangelinkcell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[15]//a')
placeexchangelink = placeexchangelinkcell.get_attribute('href')
# print(placeexchangelink)
placeexchangelink = listoffunctions.parsetheexchangelinks(placeexchangelink)
# print(placeexchangelink)

runnerscell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[16]')
runners = runnerscell.text
ratingpercentagecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[17]')
ratingpercentage = ratingpercentagecell.text
snrpercentagecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[18]')
snrpercentage = snrpercentagecell.text
arbratingpercentagecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[19]')
arbratingpercentage = arbratingpercentagecell.text
maxprofitpercentagecell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[20]')
maxprofitpercentage = maxprofitpercentagecell.text


print(dateofrace)
print(racetime)
print(racevenue)
print(horsename)
print(horseodds)
print(bookmakerlink)
print(winexchangelink)
print(placeexchangelink)
print(runners)
print(ratingpercentage)
print(snrpercentage)
print(arbratingpercentage)
print(maxprofitpercentage)
print(betamount)
print(eachway)

listoffunctions.submitthehorsebetinformation(driver,dateofrace, racetime, racevenue, horsename, horseodds, bookmakerlink, winexchangelink, placeexchangelink, runners, ratingpercentage, snrpercentage, arbratingpercentage, maxprofitpercentage, numberofplaces, betamount, eachway, bookmaker)







