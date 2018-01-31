from bs4 import BeautifulSoup
from selenium import webdriver
import requests,os

os.makedirs('imgurfolder', exist_ok=True)
userinp = input("please enter keyword of whose pics you wan't to save : ")

browser = webdriver.Chrome('/home/shivam/Downloads/chromedriver')
browser.get('https://imgur.com/')


searchElem = browser.find_element_by_class_name('search')
searchElem.send_keys(userinp)
searchElemButton = browser.find_element_by_class_name('icon-search')
searchElemButton.click()

resr = requests.get(browser.current_url)

soup = BeautifulSoup(resr.text)
imageElements = soup.select('img')


for i in range(10):
    iurl = 'http:'+imageElements[i].get('src')

    bfile = open(os.path.join('imgurfolder', os.path.basename(iurl)), 'wb')

    res = requests.get(iurl)

    for chuncks in res.iter_content(100000):
        bfile.write(chuncks)
    bfile.close()
