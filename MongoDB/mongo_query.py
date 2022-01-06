#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pymongo import MongoClient


# In[13]:


cl = MongoClient('localhost', 27017)
cl.list_database_names()


# In[14]:


db = cl.training
db.list_collection_names()


# In[17]:


# db.folk.drop()  #frop collection 'folk' inside training database


# In[25]:


coll = db.python


# In[26]:


doc = {"lab":"Accessing mongodb using python", "Subject":"No SQL Databases"}


# In[27]:


print("Inserting a document into collection.")
coll.insert_one(doc)


# In[30]:


docs = coll.find()
print("Printing the documents in the collection.")
for d in docs:
    print(d)


# In[32]:


print("Closing the connection.")
cl.close()

