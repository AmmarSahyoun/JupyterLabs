#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient


# In[4]:


cl = MongoClient('localhost', 27017)
print("Getting list of databases")
dbs = cl.list_database_names()
dbs


# In[6]:


for db in dbs:
    print(db)
print("Closing the connection to the mongodb server")
cl.close()


# In[ ]:




