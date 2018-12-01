#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests

url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'
global dict_data
dict_data={}
tp_val=[]
sailings_data=[]
global temp_data
temp_data=[]
list_data=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()

def make_data():
 temp_data=[]
 port_data=[]
 i=0
 for values in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  port_data.append(values.td.text)
  time_per=values.tr
  tp_val=[]
  for tp in time_per.find_all('td'):
   tp_val.append(tp.text)
  tp_val=[]
#  list_data.append(dict_data.copy())
  for sailings in values.find_all('tr'):
   sailings_data.append(sailings.text)
 for item in  sailings_data:
  if item!='':
   temp_data.append(item)
  else:
    dict_data['sailings']=temp_data
    dict_data['port']=port_data[i]
    temp_data=[]
    list_data.append(dict_data.copy())
    i=i+1
 for item in list_data:
  print item
if __name__=='__main__':
 make_data()
