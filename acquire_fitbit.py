#!/usr/bin/env python
# coding: utf-8

# In[77]:


import pandas as pd
import numpy as np
from datetime import datetime
import itertools

# data visualization
import matplotlib
import seaborn as sns
import statsmodels.api as sm

get_ipython().run_line_magic('matplotlib', 'inline')

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

import glob
import os


# In[78]:


cols = ['Date', 'Calories Burned', 'Steps', 'Distance', 'Floors', 'Minutes Sedentary', 'Minutes Lightly Active', 'Minutes Fairly Active', 'Minutes Very Active', 'Activity Calories']


# In[79]:


path = '~/Documents/Coding/Codeup/Coursework/ds-methodologies-exercises/time_series/fitbit/'

files = ['2018-04-26_through_2018-05-26.csv', '2018-05-27_through_2018-06-26.csv', '2018-06-27_through_2018-07-27.csv',
        '2018-07-28_through_2018-08-26.csv', '2018-08-27_through_2018-09-26.csv', '2018-09-27_through_2018-10-27.csv',
        '2018-10-28_through_2018-11-27.csv', '2018-11-28_through_2018-12-28.csv']


# In[80]:


# path = '~/Documents/Coding/Codeup/Coursework/ds-methodologies-exercises/time_series/fitbit/'                # use your path
# all_files = glob.glob(os.path.join(path, '*.csv'))     # advisable to use os.path.join as this makes concatenation OS independent

# df_from_each_file = (pd.read_csv(f, skiprows = 35, skipfooter = 310, engine = 'python') for f in all_files)
# concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
# concatenated_df
# doesn't create a list, nor does it append to one


# In[81]:


def get_fitbit():
    chunks = []
    path = '~/Documents/Coding/Codeup/Coursework/ds-methodologies-exercises/time_series/fitbit/'
    for i, element in enumerate(files):
        i = pd.read_csv(path+element, skiprows = 35, nrows=33, engine = 'python')
        chunks.append(i)
#         print(chunks)
    return chunks


# In[82]:


get_fitbit()


# In[83]:


chunks = get_fitbit()
len(chunks)


# In[84]:


chunks[1]


# In[85]:


len(chunks)


# In[100]:


def clean_fitbit():
    cols = ['Date', 'Calories Burned', 'Steps', 'Distance', 'Floors', 'Minutes Sedentary', 'Minutes Lightly Active', 'Minutes Fairly Active', 'Minutes Very Active', 'Activity Calories']
    for chunk in chunks:
        chunk.columns = cols
    return chunks


# In[101]:


clean_fitbit()


# In[86]:


chunks[3].columns = cols
chunks[3]


# In[ ]:





# In[87]:


file1 = '2018-04-26_through_2018-05-26.csv'
month1_df = pd.read_csv(path+file1, skiprows = 35, skipfooter = 310, engine = 'python', parse_dates = ['Date'], infer_datetime_format=True)


# In[88]:


month1_df


# In[89]:


file2 = '2018-05-27_through_2018-06-26.csv'
month2_df = pd.read_csv(path+file2, skiprows = 35, skipfooter = 310, engine = 'python', parse_dates = ['Date'], infer_datetime_format=True)


# In[90]:


month2_df


# ### Prepare

# In[91]:


chunks[0]


# In[98]:


def prepare():
    df = pd.DataFrame()
    data = ([chunks[i] for i in range(8)])
    df = df.append(data)
    df = df.dropna(axis=0)
    df.set_index('Date', inplace=True)
    return df


# In[99]:


prepare()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




