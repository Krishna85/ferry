#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests
from flask  import Flask,render_template
import threading

app=Flask(__name__)
url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'
global dict_data
dict_data={}
tp_val=[]
sailings_data=[]
global temp_data
temp_data=[]
global  list_data
list_data=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()

def make_data():
 threading.Timer(5.0, make_data).start()
 data=requests.get(url).text
 soup=BeautifulSoup(data,'html.parser')
 temp_data=[]
 port_data=[]
 global list_data
 list_data=[]
 i=0
 for values in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  port_data.append(values.td.text)
  for sailings in values.find_all('tr'):
   sailings_data.append(sailings.text)
 for item in  sailings_data:
  if item!='':
   temp_data.append(item[:item.find('m')+1]+' '+item[item.find('m')+1:])
  else:
    dict_data['sailings']=temp_data
    dict_data['port']=port_data[i]
    temp_data=[]
    list_data.append(dict_data.copy())
    i=i+1

@app.route("/")
def data_out():
 threading.Timer(5.0, data_out).start()
 global list_data
 #for item in list_data:
 #return item['port']
  #return item['sailings'][0]
 return render_template('home.html',data=list_data)
 list_data=[]
if __name__=='__main__':
 make_data()
 app.run()
