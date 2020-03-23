#!/usr/bin/env python
# coding: utf-8

# # Analyzing Meteorite Dataset 

# In[16]:


# imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import timeit   # for testing code runtime
from statistics import mode 
# from geopy.geocoders import Nominatim  # for geolocation conversion
import csv
import sys
sys.executable


# # Important Variables

# * meteor 
# * api_meteor_data
# * api_meteor_data_arr
# * meteor_test
# * meteor_test_2000 - 

# In[5]:


meteor = pd.read_csv('meteorite-landings.csv')
meteor = pd.DataFrame(meteor)


# print(meteor)
# print("\n\n\n")

# # print(meteor.describe())
# meteor.info()
# print("\n\n\n")

# #list all column names
# print(list(meteor.columns))

# print("\n\n\n")
# # print(meteor['fall'])

# print(np.max(meteor['year']))
# print(np.min(meteor['year']))
# print(mode(meteor['year']))


# # visualizing mass

# In[6]:



# print("Maximum mass: ", np.max(meteor['mass']))
# print("Minimum mass: ", np.min(meteor['mass']))
# print("Mean mass: ",np.mean(meteor['mass']))


# # create a figure and axis 
# fig, ax = plt.subplots() 


# # scatter the sepal_length against the sepal_width
# ax.scatter(meteor['mass'], meteor['year'])
# # set a title and labels
# ax.set_title('Meteor Dataset (mass vs year)')
# ax.set_xlabel('mass')
# ax.set_ylabel('year')


# # # Time Analysis Testing

# # In[6]:


# # Testing a time analysis function
# import timeit
# code_to_test = """
# a = range(100000)
# b = []
# for i in a:
#     b.append(i*2)
# """
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)


# # In[8]:



# bar_chart_time="""
# # create a figure and axis 
# fig, ax = plt.subplots() 


# # scatter the sepal_length against the sepal_width
# ax.scatter(meteor['mass'], meteor['year'])
# # set a title and labels
# ax.set_title('Meteor Dataset (mass vs year)')
# ax.set_xlabel('mass')
# ax.set_ylabel('year')
# """


# # 
# # # 2000 random points
# # 

# # In[7]:


# # api_meteor_data.to_csv('api_meteor_data.csv')  
# # randomly selects 2000 data points and puts them in data frame
# api_meteor_data = meteor.loc[np.random.randint(len(meteor), size = 2000)]
# print(api_meteor_data)
# print(type(api_meteor_data))


# # # Select 2000 points and save as CSV 

# # In[14]:


# meteor_test = pd.read_csv('meteorite-landings.csv')
# meteor_test_2000 = meteor.loc[np.random.randint(len(meteor), size = 2000)]

# reader = csv.DictReader(
#     open("meteor_test_2000.csv"),
#     fieldnames=['order', 'name', 'id', 'nametype', 'recclass', 'mass', 'fall', 'year', 'reclat', 'reclong', 'GeoLocation']
# )
# all_meteors = []
# for row in reader:
# #     print(row)
#     all.append(row)
# #     print(all, '\n')
# print(all)

# # all.to_csv('meteor_test_50.csv')


# # # Convert to Key : Value pairs

# # In[41]:


file = "meteor_test_2000.csv"

meteor_kv = []

with open(file, mode='r') as input_file:
    rows = []
    for row in input_file:
        rows.append(row.rstrip('\n').split(","))
    keys = rows[0]
    for values in rows[1:]:
        meteor_kv.append(dict(zip(keys, values)))

pd.set_option("display.max_rows", 1000000)
pd.set_option("display.max_columns", 1000000)
meteor_kv = pd.DataFrame(meteor_kv)
# print(meteor_kv)

# # file = "meteor_test_2000.csv"
# # meteor_kv = []
# # with open(file, mode='r') as input_file:
# #     rows = []
# #     for row in input_file:
# #         rows.append(row.rstrip('/n').split(","))
# #     keys = rows[0]
# #     for values in rows[1:]:
# #         meteor_kv.append(dict(zip(keys, values)))
# # print(meteor_kv)
# # # print(meteor_test_2000)


# # # Convert to txt file
# # 

# # In[46]:


# with open('2000_meteors.txt', 'w') as f:
#     for item in my_list:
#         f.write("%s\n" % item)


# # # Geolocation conversion

# # In[47]:


# # Testing Geolocation conversion
# geo_test = api_meteor_data_arr[2]
# geolocator = Nominatim(user_agent="api_meteor_data_arr")
# print(geo_test[9])

# location = geolocator.reverse("52.509669, 13.376294")
# print(location)
# coor = str(geo_test[9])[1:-1]
# print(coor)
# location = geolocator.reverse(coor)
# print(location)
# print(location.address)


# # # Testing graph with 2000 points 

# # In[48]:



# print("Maximum mass: ", np.max(meteor_test_2000['mass']))
# print("Minimum mass: ", np.min(meteor_test_2000['mass']))
# print("Mean mass: ",np.mean(meteor_test_2000['mass']))

# # create a figure and axis 
# fig, ax = plt.subplots() 

# # scatter the sepal_length against the sepal_width
# ax.scatter(meteor_test_2000['mass'], meteor_test_2000['year'])

# # set a title and labels
# ax.set_title('Meteor Dataset (mass vs year)')
# ax.set_xlabel('mass')
# ax.set_ylabel('year')


# # 

# # In[ ]:




