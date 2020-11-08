from selenium import webdriver
import sched, time, os, urllib.parse, re
from time import sleep
import urllib.parse
import re

def parsetheexchangelinks(urltoparse):
    urltoparse = urllib.parse.unquote(urltoparse)
    # get the string after the initial https
    print('url to parse 1 ' + urltoparse)
    urltoparse = urltoparse[4:]
    print('url to parse 2 ' + urltoparse)
    pattern = 'http'
    indexstart = int(re.search(pattern, urltoparse).span()[0])
    urltoparse = urltoparse[indexstart:-1]
    print('url to parse 3 ' + urltoparse)
    return urltoparse

def logintooddsmonkey(driver,oddsmonkeyusernameenviron,oddsmonkeypasswordenviron):
    driver.get("https://www.oddsmonkey.com/oddsmonkeyLogin.aspx?returnurl=%2f")
    sleep(3)
    driver.find_element_by_id("dnn_ctr433_Login_Login_DNN_txtUsername").send_keys(oddsmonkeyusernameenviron)
    driver.find_element_by_id("dnn_ctr433_Login_Login_DNN_txtPassword").send_keys(oddsmonkeypasswordenviron)
    driver.find_element_by_id("dnn_ctr433_Login_Login_DNN_cmdLogin").click()
    sleep(5)
    driver.get("https://www.oddsmonkey.com/Tools/Matchers/EachwayMatcher.aspx")
    sleep(3)

def logintosportsexchange(driver,sportingindexusername,sportingindexpasswordenviron):
    driver.find_element_by_id("usernameCompact").send_keys(sportingindexusername)
    driver.find_element_by_id("passwordCompact").send_keys(sportingindexpasswordenviron)
    driver.find_element_by_id("submitLogin").click()
    sleep(2)
    driver.find_element_by_xpath('//a[@class="btn-my-account"]').click()
    sleep(2)
    driver.find_element_by_id("decimalBtn").click()
    sleep(2)
    driver.get("https://www.sportingindex.com/fixed-odds/horse-racing/race-calendar")
    sleep(3)



def submitthehorsebetinformation(driver,dateofrace, racetime, racevenue, horsename, horseodds, bookmakerlink, winexchangelink, placeexchangelink, runners, ratingpercentage, snrpercentage, arbratingpercentage, maxprofitpercentage, numberofplaces, betamount, eachway, bookmaker):
    print("submitting the info however we do it - e.g. google forms etc.")

    formurltosubmitbet = "https://docs.google.com/forms/d/e/1FAIpQLSdmS2q35_jI-ZHv81uZTSLS6hdCnVnAPu7UqSCfu-rrYZXG7Q/viewform"
    driver.execute_script('window.open("' + formurltosubmitbet + '","_blank");')
    driver.switch_to.window(driver.window_handles[2])
    sleep(3)
   # print('//div[@data-params][contains(string(), "' + racetime + '")]//input')
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "dateofrace")]//input').send_keys(dateofrace)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "racetime")]//input').send_keys(racetime)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "racevenue")]//input').send_keys(racevenue)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "horsename")]//input').send_keys(horsename)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "horseodds")]//input').send_keys(str(horseodds))
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "bookmaker")]//input').send_keys(bookmakerlink)

    driver.find_element_by_xpath('//div[@data-params][contains(string(), "bookmakerlink")]//input').send_keys(bookmakerlink)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "winexchangelink")]//input').send_keys(winexchangelink)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "placeexchangelink")]//input').send_keys(placeexchangelink)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "runners")]//input').send_keys(runners)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "ratingpercentage")]//input').send_keys(ratingpercentage)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "snrpercentage")]//input').send_keys(snrpercentage)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "arbratingpercentage")]//input').send_keys(arbratingpercentage)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "maxprofitpercentage")]//input').send_keys(maxprofitpercentage)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "numberofplaces")]//input').send_keys(numberofplaces)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "eachway")]//input').send_keys(eachway)
    driver.find_element_by_xpath('//div[@data-params][contains(string(), "betamount")]//input').send_keys(str(betamount))
    sleep(3)
    driver.find_element_by_xpath('//span[text()="Submit"]').click()
    sleep(3)

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    sleep(2)


def sportingindexbetonhorse(driver,dateofrace, racetime, racevenue, horsename, horseodds, bookmakerlink, winexchangelink, placeexchangelink, runners, ratingpercentage, snrpercentage, arbratingpercentage, maxprofitpercentage, numberofplaces, betamount, eachway, bookmaker):

    betamount = str(betamount)
    driver.refresh()
    sleep(2)
    # driver.find_element_by_link_text(racetime).click()
    driver.get(bookmakerlink)
    sleep(3)
    # this is where we need to check if the horse is on this page - can happen if we choose event with same time but wrong location
    if (horsename not in driver.page_source):
        print("No horse found")
        driver.get("https://www.sportingindex.com/fixed-odds/horse-racing/race-calendar")
        sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        sleep(4)
    else:

        pathtohorsenamexpath = "//td[contains(text(), '" + horsename + "')]/following-sibling::td[5]/wgt-price-button/button"
        horseoddscontainedinthepage = driver.find_element_by_xpath(pathtohorsenamexpath).text
        horseoddscontainedinthepage = float(horseoddscontainedinthepage)
        horseodds = float(horseodds)
        # if you want to test and not submit the bet then bump up the horse odds
        # horseodds = horseodds + 7
        print ("the odds in the page are " + str(horseoddscontainedinthepage))
        print ("the odds sent from the page are " + str(horseodds))
        if horseoddscontainedinthepage >= horseodds:
            print("these are greater than or equal so we can go ahead")
            driver.find_element_by_xpath(pathtohorsenamexpath).click()
            sleep(4)
            driver.find_element_by_class_name("ng-pristine").send_keys(betamount)
            driver.find_element_by_xpath('// input[ @ type = "checkbox"]').click()
            print("found the checkbox")
            driver.find_element_by_class_name("placeBetBtn").click()
            print("placebtn clicked ok")
            sleep(5)
            driver.find_element_by_xpath("//button[contains(text(), 'Continue')]").click()
            # add the horse to the google spreadsheet update function
            # submitthehorsebetinformation(racevenue,racetime,horsename,betamount,bookmakerlink,horseodds)

            submitthehorsebetinformation(driver, dateofrace, racetime, racevenue, horsename, horseodds, bookmakerlink, winexchangelink, placeexchangelink, runners,  ratingpercentage, snrpercentage, arbratingpercentage,   maxprofitpercentage, numberofplaces, betamount, eachway, bookmaker)

        else:
            print("the odds are less so let's quit!")

        # clear variables
        horsename = ""
        racetime = ""
        racevenue = ""
        horseodds = ""
        sleep(3)
        #    driver.find_element_by_xpath('//wgt-spin-icon[@class="close-bet"]').click()
        driver.get("https://www.sportingindex.com/fixed-odds/horse-racing/race-calendar")
        sleep(2)
