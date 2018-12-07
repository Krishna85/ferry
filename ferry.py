#!/usr/bin/python
from  bs4 import BeautifulSoup
import requests
from flask  import Flask,render_template
import threading

app=Flask(__name__)
url='https://orca.bcferries.com/cc/marqui/at-a-glance.asp'
dict_data={}
list_data=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')

#print soup.prettify()

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
  
@app.route("/")
def data_out():
 make_data()
 return render_template('home.html',data=list_data)
if __name__=='__main__':
 app.run()
