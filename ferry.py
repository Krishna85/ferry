#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests

url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'

data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()

for values in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
 print(values.td.text)
 time_per=values.tr
 for tp in time_per.find_all('td'):
  print tp.text
 print('')
