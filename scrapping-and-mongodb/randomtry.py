from os import replace
import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

URL = "https://www.swansea.ac.uk/staff/engineering/bache-m-r/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
div = soup.find('div', {"class" : "col"})
text = div
print()
