from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

class Scrap():

    def ScrapData(self, url, item1, item2, item3, item4):
        self.url=url

        self.driver = webdriver.Chrome("chromedriver.exe")

        self.driver.get(self.url)

        time.sleep(2)

        self.Data1=[]

        self.Data2=[]

        self.Data3=[]

        self.driver.get(self.url)

        self.content=self.driver.page_source

        self.soup=BeautifulSoup(self.content)

        for i in soup.findAll('i', href=True, attrs={'class':item1}):
            self.data1=i.find('div', attrs={'class':item2})
            self.data2=i.find('div', attrs={'class':item3})
            self.data3=i.find('div', attrs={'class':item4})
            self.Data1.append(self.data1.text)
            self.Data2.append(self.data2.text)
            self.Data3.append(self.data3.text)

        self.df=pd.DataFrame({'coulmn_name':self.Data1,'coulmn_name':self.Data2,'column_name':self.Data3})

        self.df.to_csv('data.csv', index=False, encoding='utf-8')
