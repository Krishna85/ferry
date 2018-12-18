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
new_list=[]
data=requests.get(url).text
soup=BeautifulSoup(data,'html.parser')


def make_data():
 data=requests.get(url).text
 soup=BeautifulSoup(data,'html.parser')
 list_data=[]
 global new_list
 new_list=[]
 for value in soup.find_all('tr',bgcolor=['#D4E3ED','#dfeaf2']):
  for item in value.find_all('td'):
   a=item.text.encode('ascii','ignore').strip('\n')
   if not a.isspace() and  a!="":
     list_data.append(a)
  dict_data={}
  dict_data['terminal']=list_data[0]
  if 'm' in list_data[1]:
   dict_data['tp']=list_data[1][:list_data[1].find('m')+1]+' '+list_data[1][list_data[1].find('m')+1:]
  else:
   dict_data['tp']=list_data[1]
  dict_data['cw']=list_data[-3]
  dict_data['ow']=list_data[-2]
  dict_data['ls']=list_data[-1]
  new_list.append(dict_data)
  list_data=[]

@app.route("/")
def data_out():
 make_data()
 return render_template('home.html',data=new_list)
if __name__=='__main__':
 app.run(host='0.0.0.0',port='80')


