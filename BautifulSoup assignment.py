#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(page.content)
soup
titles = []

for i in soup.find_all('span', class_='mw-headline'):
    titles.append(i.text)
    
print(len(titles))
import pandas as pd
df = pd.DataFrame({'Headers':titles})
df


# In[3]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://presidentofindia.nic.in/former-presidents')
soup = BeautifulSoup(page.content)
soup
names = []

for i in soup.find_all('div', class_='desc-sec'):
    names.append(i.text)
    
print(len(names))
import pandas as pd
df = pd.DataFrame({'Former President list':names})
df


# In[5]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.icc-cricket.com/teams/men')
soup = BeautifulSoup(page.content)
soup
teams = []

for i in soup.find_all('div', class_='font-h3-upper text-center text-dark-label'):
    teams.append(i.text)
teams

print(len(teams))

import pandas as pd
df = pd.DataFrame({'Top 10 teams':teams})
df


# In[14]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.cnbc.com/world/?region=world')
soup = BeautifulSoup(page.content)
soup

headline = []

for i in soup.find_all('a', class_="LatestNews-headline"):
    headline.append(i.text)
    headline
    
time = []

for i in soup.find_all('time', class_="LatestNews-timestamp"):
    time.append(i.text)
    time
    
print (len(time))
import pandas as pd
df = pd.DataFrame({'Time':time})
df

print (len(headline),len(time))
import pandas as pd
df = pd.DataFrame({'Headlines':headline,'Time':time})
df


# In[18]:


import requests
from bs4 import BeautifulSoup

url = 'https://www.cnbc.com/world/?region=world'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

links = []
for i in soup.find_all('a'):
    print(i.get('href'))
    
import pandas as pd
df =pd.DataFrame({'URL':link})
df


# In[17]:


from bs4 import BeautifulSoup
import requests
page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
soup = BeautifulSoup(page.content)
soup

name = []

for i in soup.find_all('div',class_="restnt-info cursor"):
    name.append(i.text)
    name
    
location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
         location.append(i.text)
         location
        

rating = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):  
         rating.append(i.text)
         rating
            
pic = []
for i in soup.find_all('img',class_="no-img"):
         pic.append(i['data-src'])
         pic
            
food = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
         food.append(i.text)
         food            
    
print (len(name),len(location),len(rating),len(pic),len(food))
import pandas as pd
df = pd.DataFrame({'Restaurent name':name,'Location':location,'Cousine':food,'Ratings':rating,'Image URL':pic})
df


# In[ ]:




