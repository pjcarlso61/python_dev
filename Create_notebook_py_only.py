#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from datetime import datetime


# In[2]:



notebook_path = os.path.join(os.getcwd(),'Create_notebook_py_only.ipynb')

#Bash:
get_ipython().system('jupyter nbconvert --to script {notebook_path}')

