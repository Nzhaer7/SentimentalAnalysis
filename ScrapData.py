from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

url=""

driver = webdriver.Chrome("./chromedriver.exe")

Data1=[]

Data2=[]

Data3=[]

driver.get(url)

content=driver.page_source

soup=BeautifulSoup(content)

for i in soup.findAll('i', href=True, attrs={'class':''}):
    data1=i.find('div', attrs={'class':''})
    data2=i.find('div', attrs={'class':''})
    data3=i.find('div', attrs={'class':''})
    Data1.append(data1.text)
    Data2.append(data2.text)
    Data3.append(data3.text)

df=pd.DataFrame({'coulmn_name':Data1,'coulmn_name':Data2,'column_name':Data3})

df.to_csv('data.csv', index=False, encoding='utf-8')