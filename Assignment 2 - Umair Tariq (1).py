#!/usr/bin/env python
# coding: utf-8

# In[1]:


8 + 34 / 5 - 7 + 45 * 4**5 + 12 /35 + (23 -12) * 34 + 98 **3 - 23 - 98 / 32 * (2 * 7) - 22 + 21 * 45 - 2 - 1 


# In[12]:


a = 3
if a > 12:
    print('yes greater value')
else:
    print('less value')


# In[ ]:





# In[13]:


a = 3
if a < 12:
    print('yes greater value')
else:
    print('less value')


# In[14]:


a = 3
if a >= 3:
    print('yes greater or equal value')
else:
    print('less value')


# In[15]:


a = 3
if a >= 3:
    print('yes greater or equal value')
else:
    print('less value')


# In[16]:


a = 'umair tariq'
dir(a)


# In[17]:


a = 'umair tariq'
a.swapcase()


# In[18]:


a = 'umair tariq'
a.title()


# In[19]:


a = 'umair tariq'
a.lower()


# In[20]:


a = 'umair tariq'
a.upper()


# In[21]:


a = 'umair tariq'
a.strip(3)


# In[22]:


a = 'umair tariq'
a.strip()


# In[23]:


a = 'umair tariq'
a.strip(0:2)


# In[24]:


a = 'umair tariq'
a.strip('umair')


# In[27]:


a = 'umair tariq'
a.split()


# In[28]:


a = 'umair tariq'
a.strip()


# In[32]:


a = 'umair tariq'
a.rstrip(a)


# In[34]:


a = 'umair tariq'
a.partition('*')


# In[35]:


a = 'umair tariq'
a.partition(' ')


# In[36]:


a = '           umair tariq          '
a.rstrip()


# In[37]:


a = '              umair tariq     '
a.lstrip()


# In[39]:


a = 'umair tariq'
a.join('abc')


# In[40]:


a = 'umair tariq'
a.istitle()


# In[41]:


a = 'uMair tAriq'
a.istitle()


# In[43]:


a = 'Umair Tariq'
a.istitle()


# In[46]:


a = 'uMair tAriq'
a.isspace()


# In[47]:


a = '      '
a.isspace()


# In[48]:


a = '        uMair     tAriq      '
a.isspace()


# In[49]:


a = 'uMair tAriq'
a.isdigit()


# In[51]:


a = '234'
a.isdigit()


# In[56]:


a = 'uMair tAriq'
a.ljust(5,'d')


# In[58]:


a = 'uMairtAriq'
a.isalpha()


# In[59]:


a = 'uMair tAriq'
a.center(2)


# In[64]:


a = 'uMairtAriq'
a.center(1)


# In[65]:


a = 'uMair tAriq'


# In[76]:


a = 'umair umair is a good boy and tAriq is also a good boy and father of umair'
a.count('umair')


# In[77]:


a = '1111Mai1120000nmsddjjdjddr tA1200992r123i24q8'
a.isnumeric()


# In[80]:


a = 'uMair tAriq'
a.format_map(1)


# In[81]:


a = 'uMair tAriq'
a.casefold()


# In[1]:


a = 'uMair tAriq'
a.isspace() #to check for the whitespace characters in a line


# In[7]:


a = 'uMair tAriq a sasdsadsadasdsadassaa'
a.ljust(90,'*') #used to fill the empty spaces with characters specified


# In[20]:


a = 'uMair tAriqiiiiiiiiiiiiiiiiiiiii'
a.find('A')


# In[ ]:




