#!/usr/bin/env python
# coding: utf-8

# In[88]:


pip install matplotlib


# In[89]:


import numpy as np


# In[90]:


pip install matplotlib


# In[91]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[92]:


x=[1,2,3,4,5]
y=[10,12,8,15,7]

#creating a Line plot
plt.plot(x,y);


# In[93]:


plt.plot(x,y)

#adding Lables to the axes and Title
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Basic Line Plots')

plt.show()


# In[94]:


#adding linestyle and color
plt.plot(x,y, linestyle='-', color='red', marker='o');


# In[95]:


plt.plot(x, y, 'b+');


# In[96]:


plt.plot(x,y, 'bo');


# In[97]:


plt.plot(x,y, 'r+');


# In[98]:


#adding a specific linestyle and color
plt.plot(x,y, marker='o')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.title('Customized Line Plots')
plt.plot()

#to specify the lower and upper limits
plt.xlim(0.4)
plt.ylim(0,15)
plt.show()


# In[99]:


plt.savefig('plot1.png')


# In[100]:


# creating the raw data
categories = ['A','B','C','D']
value = np.array([25, 40, 15, 30])

# ploting it
plt.xlabel('categories')
plt.ylabel('value')
plt.title('BAR PLOT')
plt.bar(range(0,4), value)
plt.xticks(range(0, 4),categories)
plt.show()


# In[101]:


pip install seaborn


# In[102]:


import seaborn as sns


# In[103]:


#creating a histogram these pointdata

Data = [32, 45, 50, 28,36, 42,38, 25, 29, 5, 6,48, 60]

sns.histplot(Data, bins=14, kde=True)
plt.xlabel('Data')
plt.ylabel('count')
plt.title('Histogram')
plt.show()


# In[104]:


# scatterplot: using some points for it
X = [3, 5, 7, 10, 12,15]
Y = [25, 40, 30, 50, 35, 60]
sns.scatterplot(x=[3, 5, 7, 10, 12,15], y= [25, 40, 30, 50, 35, 60])
plt.title('SCATTERPLOT')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.show()


# In[105]:


# A Pie Chartable
labels = ['Apples', 'Bananas', 'Oranges', 'Grapes'] 
sizes = [30, 25, 20, 15]

y = sizes

plt.pie(y, labels= labels, autopct='%.0f%%')
plt.title('PIE CHARTABLE')
plt.show()


# In[106]:


# Creating a Box plot
poindata= [45, 60, 75,300, 80,350, 90, 95, 100, 110, 120,250,200]
sns.boxplot(data)
plt.title('BOX PLOT')
plt.xlabel('x-axis label')
plt.ylabel('y-axis label')
plt.show()


# In[107]:


import pandas as pd


# In[109]:


#MAKING A BARH PLOT
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 15, 30]

df = pd.DataFrame({'Categories':['A', 'B', 'C', 'D'],
       'Values': [25, 40, 15, 30]})

best = df.plot.barh(x='Categories', y='Values')
plt.title('BARH PLOT')
plt.show()


# In[ ]:


# thank you. it was nice making such an attempt.Getting better always.

