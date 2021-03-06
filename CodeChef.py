
# coding: utf-8

# In[1]:

import bs4
from bs4 import BeautifulSoup as BS
import requests


# In[2]:

class info():
    def __init (self):
        pass
    def __init__(self, name, username, college, ratings):
        self.longrating = ratings[0]
        self.shortrating = ratings[1]
        self.ltimeallratings = ratings[2]
        self.name = name
        self.username = username
        self.college = college


# In[3]:

listofusername = ['vaibhavccrox', 'shadycoder', 'yash_mittal', 'saragarwal']
allinfo = []


# In[4]:

for iz in listofusername:
    url = 'https://www.codechef.com/users/' + iz
    data = requests.get(url)
    soup = BS(data.text,'html.parser')
    na = soup.find_all('table')
    name = (na[1].find_all('div'))[1].text
    li = na[0].find_all('table')
    useful = li[1]
    td = useful.find_all('td')
    username = td[1].text
    cnt = td[5].text
    college = td[13].text
    useful = na[5].find_all('tr')
    ratings = []

    for ix in range(1,len(useful)):
        td = useful[ix].find_all('td')
        text=td[2].text.encode('UTF-8')
        text = str(text)
        string = ''
        for iy in text:
            if iy>='0' and iy<='9':
                string = string + iy
            else:
                break
        ratings.append(string)
    #OBJECT CREATION
    allinfo.append(info(name,username, college,ratings))


# In[6]:

print 'Name\t\t\tUsername\t\t\tLong Rating'
counter = 0
for ix in allinfo:
    if counter is not 3:
        print ix.name,'\t\t',ix.username,'\t\t\t',ix.longrating
    else:
        print ix.name,'\t',ix.username,'\t\t\t',ix.longrating
    counter += 1

