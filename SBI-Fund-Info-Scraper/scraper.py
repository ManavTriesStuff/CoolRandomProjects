import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

## Checking PATH 
# path = os.getenv('PATH') 
# print(path)

URL = 'https://www.sbipensionfunds.com/historical-nav/'

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
# page = requests.get(URL,headers=headers)

# soup = BeautifulSoup(page.content,'html.parser')
# # print(soup.prettify())

# print(soup.find_all('table'))


# table = pd.read_html(soup)
# print(table)

# Date = soup.find_all('Date')
# CG_Scheme = soup.find_all('CG Scheme')
# SG_Scheme = soup.find_all('SG Scheme')
# E_Tier_I = soup.find_all('E Tier I')
# C_Tier_I = soup.find_all('C Tier I')
# G_Tier_I = soup.find_all('G Tier I')

# data = []
# for i in range(0,len(Date)):
#    rows = [Date[i].get_text(),CG_Scheme[i].get_text(),
#            SG_Scheme[i].get_text(),E_Tier_I[i].get_text(),
#            C_Tier_I[i].get_text(), G_Tier_I[i].get_text()]
#    data.append(rows)

# df = pd.DataFrame(data, columns = ['Date','CG_Scheme',
#                                   'SG_Scheme','E_Tier_I','C_Tier_I',
#                                   'G_Tier_I'], dtype = float)
# print(df)


# Using Selenium's Chrome Driver
driver = webdriver.Chrome('D:\\Workspace\\ChromeDriver\\chromedriver.exe')
driver.get(URL)


text_input1 = driver.find_element_by_id("f_date_p1")
text_input1.send_keys("10-10-2020")
text_input2 = driver.find_element_by_id("f_date_p2")
text_input2.send_keys("10-10-2021")
search_button = driver.find_element_by_name("mysubmit")
search_button.click()
driver.page_source

doc = BeautifulSoup(driver.page_source, "html.parser")
# print(doc.prettify())

table = doc.find_all('table')
# print(len(table))
data = pd.read_html(str(table))[1]
# print(data)

df = data
print(df)
# data = pd.DataFrame()

df.to_csv('sbi.csv', encoding='utf-8', index=False)

driver.close()


