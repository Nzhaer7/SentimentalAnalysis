from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time

url=""

driver = webdriver.Chrome("./chromedriver.exe")

content=driver.page_source

soup=BeautifulSoup(content)

df=pd.DataFrame()

df.to_csv('data.csv', index=False, encoding='utf-8')

data=[]

driver.get(url)