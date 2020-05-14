#!/usr/bin/env python
# coding: utf-8

# # ***Premise***
# ---
# ---

# In[ ]:





# # ***Questions***
# ---
# ---

# + **Easy**
#     + Which year had the most meteors?
#         - _2013_
#     + What is the average mass of a meteors we've observed?
# + **Hard**
#     + Are there more meteors around the equator or the poles?
#     + What time of year got the most asteroids? (Noticable trends in year data)
# + **Other**
#     + How many meteors fell in important years (birth year(1995), Y2K, 2008(Obama), 2020(Now))?
# 

# # ***Concepts to cover***
# ---
# ---

# - [x] Histograms
# - [ ] PDF
# - [ ] CDF
# - [ ] Hypothesis Testing
# - [ ] Confidence Interval
# - [ ] Correlation
# - [ ] Outliers
# - [ ] Normal Distribution
# - [ ] Time Analysis

# # ***Imports***
# ---
# ---

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import plotly.express as px
from geopy.geocoders import Nominatim
import geopy as gp
from datetime import datetime


# # ***Data***
# ---
# ---

# In[17]:


data = pd.read_csv('data/meteorite-landings.csv')
# data = pd.read_csv('../data/Meteorite_Landings.csv')
print(data.columns)

data.head()


# ## Basic Statistics

# In[18]:


print("Data described: \n")
print(data.describe())
print('\n')
print("Data info: \n")
print(data.info())


# *Conclusions / Questions*
#     - There are missing values in mass, year, and locations
#     - Appropriate data types thus far

# # ***Cleaning***
# ---
# ---
# 

# ## Rename columns

# In[19]:


data.rename(columns={'recclass':'class', 'reclat':'lat', 'reclong':'long', 'mass (g)':'mass'}, inplace=True)
data


# *Conclusions / Questions*
#     - ...

# ## Outliers

# In[20]:


sns.boxplot(x=data['year'])


# In[21]:


fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(data['year'], data['mass'])
# ax.set_xlabel('Proportion of non-retail business acres per town')
# ax.set_ylabel('Full-value property-tax rate per $10,000')
plt.show()


# # ***Statistical Plotting***
# ---
# ---

# ## Fall vs Fallen Histogram

# In[22]:


data['fall'].hist(bins=3)  # 
plt.show()


# *Conclusions / Questions*
#     - ...

# ## Equator or Poles

# In[23]:


plt.scatter(data.mass, data.lat)
# print(data[data['lat']>0].count())
# print(data[data['lat']<0].count())
axes = plt.gca()
axes.set_ylim([-90,90])
above_equator = data[data.lat >0].shape[0]
at_equator = data[data.lat ==0].shape[0]
below_equator = data[data.lat <0].shape[0]
plt.show()

print("Above Equator:", above_equator, '\n')
print("At Equator:", at_equator, '\n')
print("Below Equator:", below_equator, '\n')

labels = ["Above", 'At', 'Below']
values = [above_equator, at_equator, below_equator]
plt.pie(values, labels=labels)
plt.show()


# *Conclusions / Questions*
#     - There are missig values because of the `Nan` values that I didn't remove. If I do remove then and replace them with 0, then it'ss alter results of values that actually are on the equator or prime meridian

# ## Box Plot

# *Conclusions / Questions*
#     - ...

# ## PDF

# In[10]:


sns.distplot(data['year'].dropna(), hist=True, kde=True, bins=16)


# *Conclusions / Questions*
#     - ...

# ## CDF

# In[24]:


ls_year = data['year'].dropna().values

def calculate_cdf(x, threshold):
    return np.sum(x <= threshold)

# Create an array cdf_age where each value is the cdf of the age for each threshold
cdf_year = [calculate_cdf(ls_year, r)/len(ls_year) for r in range(int(np.min(ls_year)), int(np.max(ls_year)))]

plt.plot(range(int(np.min(ls_year)), int(np.max(ls_year))), cdf_year)


# *Conclusions / Questions*
#     - ...

# ## Violin Plot

# In[12]:


sns.violinplot(x="year", y="mass", data=data)


# *Conclusions / Questions*
#     - Why are the masses in the violin plot negative?

# ## Correlation

# In[13]:


sns.heatmap(data.corr(), annot=True, cmap='coolwarm')


# *Conclusions / Questions*
#     - Why are the masses in the violin plot negative?

# # ***Various Plotting***
# ---
# ---

# ## See the top 10 classification of meteors

# In[14]:


top_10_class = data['class'].value_counts()[:10]
plt.bar(top_10_class, height = 1)

top_10_class.plot(kind='bar')


# *Conclusions / Questions*
#     - ...

# ## Lat and Long scatter plot, using mass as bubble size
# - ***Latitude are y values  (90 through -90)***
# - ***Longitude are x values (-180 to 180)***

# In[25]:


plt.figure(figsize=(10,7))
N = len(data['mass'])
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
colors = np.random.rand(N)
plt.scatter(data['long'], data['lat'], s=area, c=colors, alpha=0.2)

plt.grid(True)
axes = plt.gca()
axes.set_xlim([-90,90])
axes.set_ylim([-180,180])
plt.show()


# *Conclusions / Questions*
#     - ...

# ## Geolocation Function using geopy
# 

# In[ ]:


# geolocator = Nominatim(user_agent="project_impact")
# coor=gp.Point(data['lat'][1], data['long'][1])
# location = geolocator.reverse(coor)
# print(location.raw['address'].get('country'))


# ## Geolocations loop

# In[ ]:


# lists = []
# for i in range(20):
#     lats = data['lat'].get(key = i)
#     longs = data['long'].get(key = i)
#     coor = gp.Point(lats, longs)
#     country = geolocator.reverse(gp.Point(coor)).raw['address'].get('country')
#     lists.append(country)
# print(lists)


# ## Year Value Counts

# In[16]:


print(data['year'].value_counts())
# data['recclass'].value_counts().plot(kind='bar')  # bar chart of the amount embarked passengers by class


# ## Time Analysis

# In[17]:


data['year'].fillna(0).astype(int)


# *Conclusions / Questions*
#     - ...

# In[18]:


year_count = data.groupby('year')['year'].count()
plt.figure(figsize=(10,8))
plt.plot(year_count)
print("Years describes: ", year_count.describe(), '\n')
print("Confirming amount of unique year", data.year.nunique(), '\n')
print("Year with most recorded data:", data.year.max())
print("Total span of year data: ", data.year.max()-data.year.min(), 'years\n')
# plt.hist(year_count)


# *Conclusions / Questions*
#     - ...
