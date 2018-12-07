#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests
from flask  import Flask,render_template
import threading
import re
app=Flask(__name__)
url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'
dict_data={}
list_data=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()
#EXTRAS Added!

def make_data():
 data=requests.get(url).text
 soup=BeautifulSoup(data,'html.parser')
 temp_data=[]
 port_data=[]
 sailings_data=[]
 global list_data
 list_data=[]
 global dict_data
 dict_data={}
 i=0
 for values in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  port_data.append(values.td.text)
  for sailings in values.find_all('tr'):
   sailings_data.append(sailings.text)
 for item in  sailings_data:
  if item!='':
   temp_data.append(item[:item.find('m')+1]+' '+item[item.find('m')+1:])
  else:
    try:
     dict_data['sailings']=temp_data
     dict_data['port']=port_data[i]
     temp_data=[]
     list_data.append(dict_data.copy())
     i=i+1
    except:
     pass
 new_list=[]
 for value in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  for item in value.find_all('td'):
   try:
    if 'full' not in item.div.text and item.div.text!= "" and '\n' not in item.div.text:
    # print item.div.text
     print('-----------------------')
     new_list.append(item.div.text)
   except:
    pass  
  for item in value.find_all('a', href=re.compile('src=ltr$')):
   new_list.append(item.text)
 print new_list
#@app.route("/")
def data_out():
 make_data()
if __name__=='__main__':
 data_out()
