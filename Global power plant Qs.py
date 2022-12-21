#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np


# In[3]:


dataset=pd.read_csv(r"C:\Users\swara\Downloads\global_power_plants.csv")


# In[4]:


dataset


# In[26]:


dataset.info()


# In[6]:


## Find the country who has primary fuels as hydro and get the avg capacity of megawatt of each country?


# In[7]:


data=dataset.loc[dataset["primary_fuel"]=="Hydro"]


# In[8]:


data


# In[19]:


data1=data[["country","primary_fuel"]]


# In[20]:


data1


# In[23]:


dataset


# In[30]:


dataset["capacity in MW"]=dataset["capacity in MW"].str.replace("$","")


# In[32]:


dataset


# In[33]:


dataset["capacity in MW"]=pd.to_numeric(dataset["capacity in MW"])


# In[34]:


dataset.info()


# In[35]:


data=pd.pivot_table(dataset,index="country")


# In[36]:


data


# In[39]:


data1=pd.pivot_table(data,index=["country","capacity in MW"],aggfunc=[np.mean])


# In[40]:


data1


# In[ ]:





# In[ ]:




