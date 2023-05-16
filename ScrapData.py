import requests
from bs4 import BeautifulSoup
import csv


URL = ""

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

context = soup.find(id="")

data=context.text.strip()


