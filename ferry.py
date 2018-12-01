#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests

url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'
global dict_data
dict_data={}
tp_val=[]
list_data=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()

def make_data():
 for values in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  dict_data['ports']=values.td.text
  time_per=values.tr
  tp_val=[]
  for tp in time_per.find_all('td'):
   tp_val.append(tp.text)
#  print tp_val
  dict_data['time']=tp_val[0]
  dict_data['per']=tp_val[1]
  print dict_data
  list_data.append(dict_data)
  print('--------------------------------------------------------------------')
  print(list_data)
  print('*******************************************************************')
if __name__=='__main__':
 make_data()
