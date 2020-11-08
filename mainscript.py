from selenium import webdriver
import sched, time, os, urllib.parse, re
from time import sleep
import listoffunctions
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys
# set variables
driver = webdriver.Chrome(executable_path="c:\se\chromedriver.exe")
refresh_time_in_seconds = 20
betamount = 1
logintosportingindex = 1
logintooddsmonkey = 1
eachway = 1
# need to sort number of places in future - get from the page race detail page
numberofplaces = 4

sportingindexusername = os.environ.get("sportingindexuname")
sportingindexpasswordenviron = os.environ.get("sportingindexpasswd")
oddsmonkeyusernameenviron = os.environ.get("oddsmonkeyusername")
oddsmonkeypasswordenviron = os.environ.get("oddsmonkeypassword")

# log into oddsmonkey
if logintooddsmonkey:
    listoffunctions.logintooddsmonkey(driver,oddsmonkeyusernameenviron,oddsmonkeypasswordenviron)

# log into sportingindex
if logintosportingindex:
    driver.execute_script('window.open("https://www.sportingindex.com/fixed-odds","_blank");')
    driver.switch_to.window(driver.window_handles[-1])
    sleep(3)
    listoffunctions.logintosportsexchange(driver,sportingindexusername,sportingindexpasswordenviron)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    sleep(4)


url = driver.current_url
while True:
    if url == driver.current_url:
        driver.refresh()
        sleep(4)
        if not driver.find_elements_by_class_name("rgNoRecords"):
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

            horseoddscell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[13]')
            horseodds = horseoddscell.text

            bookmakerlinkcell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[10]//a')
            bookmakerlink = bookmakerlinkcell.get_attribute('href')
            bookmakerlink = listoffunctions.parsetheexchangelinks(bookmakerlink)
            print ("bookmaker linnk is " + bookmakerlink)
            bookmaker = bookmakerlink

            winexchangelinkcell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[14]//a')
            winexchangelink = winexchangelinkcell.get_attribute('href')
            winexchangelink = listoffunctions.parsetheexchangelinks(winexchangelink)

            placeexchangelinkcell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[15]//a')
            placeexchangelink = placeexchangelinkcell.get_attribute('href')
            # print(placeexchangelink)
            placeexchangelink = listoffunctions.parsetheexchangelinks(placeexchangelink)
            # print(placeexchangelink)

            runnerscell = driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[16]')
            runners = runnerscell.text
            ratingpercentagecell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[17]')
            ratingpercentage = ratingpercentagecell.text
            snrpercentagecell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[18]')
            snrpercentage = snrpercentagecell.text
            arbratingpercentagecell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[19]')
            arbratingpercentage = arbratingpercentagecell.text
            maxprofitpercentagecell = driver.find_element_by_xpath(
                '//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[20]')
            maxprofitpercentage = maxprofitpercentagecell.text

            driver.find_element_by_xpath('//table//tr[@id="dnn_ctr1157_View_RadGrid1_ctl00__0"]//td[55]//div//a').click()
            # driver.find_element_by_id("submitLogin").click()
            # print(dateofrace + "," + racetime + "," + racevenue + "," + horsename + "," + horseodds + "," + bookmakerlink)

            url = driver.current_url
            driver.switch_to.window(driver.window_handles[1])

            listoffunctions.sportingindexbetonhorse(driver,dateofrace, racetime, racevenue, horsename, horseodds, bookmakerlink, winexchangelink, placeexchangelink, runners, ratingpercentage, snrpercentage, arbratingpercentage, maxprofitpercentage, numberofplaces, betamount, eachway, bookmaker)

            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            sleep(3)
        else:
            print("nothing to see here")
            # so no log out
            driver.switch_to.window(driver.window_handles[1])
            sleep(4)

            driver.get("https://www.sportingindex.com/fixed-odds/horse-racing/race-calendar")
            sleep(2)
            driver.switch_to.window(driver.window_handles[0])
            driver.refresh()
            sleep(4)
        time.sleep(refresh_time_in_seconds)
        print("waiting")
