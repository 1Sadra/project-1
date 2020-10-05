#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time, random, requests


# In[17]:


from bs4 import BeautifulSoup


# In[18]:


import re


# In[4]:


movies_list = []
urls = ["https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies1.html", "https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies2.html", "https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies3.html"]
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", href = True):
        movies_list.append(link["href"])
for movie in range(30001):
    response = requests.get(movies_list[movie])
    if int(response.status_code) == 200:
        time.sleep(random.randint(1, 5))
    elif int(response.status_code) == 429:
        time.sleep(1200)
    soup = BeautifulSoup(response.text, "html.parser")
    name = "article_{0}.html".format(movie)
    page = str(soup)
    with open(name, "a") as f:
        f.write(page)


# In[51]:


for film in range(6):
    with open("article_{0}.html".format(film), "r") as r:
        read = r.read()
        soup1 = BeautifulSoup(read, "html.parser")
        Title = []
        for h1 in soup1.find_all("h1"):
            Title.append(h1.text) # finish Title
        intro = []
        for par in soup1.find_all("p")[:1:]:
            intro.append(par.text) # finish intro
        plot = []
        for par in soup1.find_all("p")[1:2:]:
            plot.append(par.text) # finish plot
        film_name = []
        t = soup1.find_all("tbody")
        for tbody in t:
            for th in tbody.find_all("th", class_ = "summary"):
                print(th.text)
        if tbody not in t:
            print("NA")


# In[64]:


for film in range(6):
    with open("article_{0}.html".format(film), "r") as r:
        read = r.read()
        soup1 = BeautifulSoup(read, "html.parser")
        Title = []
        for h1 in soup1.find_all("h1"):
            Title.append(h1.text) # finish Title
        intro = []
        for par in soup1.find_all("p")[:1:]:
            intro.append(par.text) # finish intro
        plot = []
        for par in soup1.find_all("p")[1:2:]:
            plot.append(par.text) # finish plot
        for tbody in soup1.find_all("tbody"):
            if tbody not in soup1.find_all("tbody"):
                print("NA")
            else:
                for th in tbody.find_all("th", class_ = "summary"):
                    print(th.text)


# In[ ]:




