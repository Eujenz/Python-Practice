#!/usr/bin/env python
# coding: utf-8

# In[50]:


from selenium import webdriver
driver = webdriver.Chrome('C:/Users/Lee CHIENWEI/AppData/Local/Programs/Python/Python38-32/Scripts/chromedriver.exe')
driver.get('http://www.kuman5.com/20454/1133682.html')


# In[51]:


for _ in range(20):
    import time
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# In[52]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')


# In[53]:


import re
soup.find_all(src=lambda src: src and re.compile(r"^https://p.pstatp.com/origin").search(src))


# In[ ]:





# In[ ]:




