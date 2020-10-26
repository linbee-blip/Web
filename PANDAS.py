#!/usr/bin/env python
# coding: utf-8

# In[108]:


import numpy as np
import cvxpy as cv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import pandas as pd


# In[109]:


bf = pd.DataFrame({
    "Name" : ["Pentsiwah, Miss Linda",
             " Sarfo, Mr. Kojo",
             "Baah, Mr. Bernard"],
"Age": [ 22, 23, 24],
"Sex": ["Female", "Male", "Male"]}
)


# In[110]:


bf


# In[ ]:





# In[111]:


df = pd.DataFrame({
    "Name": ["Things Fall Apart", "Americanah", "Animal Farm"],
    "Author": ["Chinua Achibe", "Chiamanda", "Owens"],
    "Year": ["1998", "1993","1995"]}
)


# In[112]:


df


# In[113]:


df["Name"]


# In[114]:


df["Year"]


# In[115]:


yeares =pd.Series([1995,1998,1996], name="Years")


# In[116]:


yeares


# In[117]:


yeares.max()


# In[118]:


df["Year"].max()


# In[119]:


bf["Age"].max()


# In[120]:


bf.describe()


# In[121]:


bf["Age"].min()


# In[122]:


df.describe()


# In[123]:


bf["Age"]


# In[ ]:





# In[124]:


url = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv'
qf = pd.read_csv(url,index_col=0)

print (qf.head(25))


# In[125]:


qf


# In[126]:


print (qf.head(8))


# In[127]:



print (qf.tail(8))


# In[128]:


qf.dtypes


# In[129]:


qf.to_excel('titanic.xlsx', sheet_name='passengers', index=False)


# In[130]:


qf = pd.read_excel('titanic.xlsx', sheet_name='passengers')


# In[131]:


qf


# In[132]:


qf["Name"]


# In[133]:


qf["Name"].head(8)


# In[134]:


qf.describe()


# In[135]:


qf.info()


# In[136]:


qf["Age"]


# In[137]:


ages = qf["Age"]


# In[138]:


ages


# In[139]:


ages.head()


# In[140]:


ages.tail()


# In[141]:


type(qf["Age"])


# In[142]:


qf["Age"].shape


# In[143]:


age_sex = qf[["Age", "Sex"]]


# In[144]:


age_sex.head()


# In[145]:


qf[["Age", "Sex"]].shape


# In[146]:


above_35 = qf[qf["Age"]>35]


# In[147]:


above_35.head()


# In[148]:


female_passengers = qf[qf["Sex"] == "female"]


# In[149]:


female_passengers.tail()


# In[ ]:





# In[150]:


age_sex = qf[["Age", "Sex"]]


# In[151]:


age_sex


# In[152]:


gentle_men = qf[qf["Sex"] == "male"]


# In[153]:


gentle_men


# In[154]:


cabin_class = qf[qf["Pclass"] == 2 | (qf["Pclass"] == 3)]


# In[155]:


cabin_class


# In[156]:


passenger_names = qf.loc[qf["Age"]> 35, "Name" ]


# In[157]:


passenger_names


# In[158]:


passenger_cl = qf.loc[qf["Age"] == 35, "Pclass"]


# In[159]:


passenger_cl


# In[160]:


qf.iloc[ 9:25, 3:5]


# In[161]:


qf.iloc[0:3,3] = "anonymous"


# In[162]:


qf.tail()


# In[163]:


url ="https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/air_quality_no2.csv"

air_quality = pd.read_csv(url,index_col=0)

print (air_quality)


# In[ ]:





# In[164]:


air_quality.plot()


# In[165]:


air_quality["station_paris"].plot()


# In[166]:


air_quality["station_antwerp"].plot()


# In[167]:


air_quality.plot.scatter(x="station_london",
                        y= "station_paris",
                        alpha = 0.5)


# In[168]:


air_quality.plot.scatter(x="station_antwerp",
                        y="station_paris",
                        alpha =0.5)


# In[169]:


air_quality.plot.box()


# In[ ]:





# In[170]:


[method_name for method_name in dir(air_quality.plot)
 if not method_name.startswith("_")]


# In[ ]:





# In[171]:


axs = air_quality.plot.area(figsize=(15, 5), subplots=True)


# In[172]:


fig, axs = plt.subplots(figsize=(20,5));
air_quality.plot.area(ax=axs)
axs.set_ylabel("Nitrogen");
axs.set_xlabel("Date");
fig.savefig("nitrogen.png")


# In[ ]:





# In[174]:


air_quality["london_mg_per_cubic"] = air_quality["station_london"]
air_quality.head()


# In[181]:


air_quality["ratio_paris_antwerp"] = air_quality["station_paris"] / air_quality["station_antwerp"]

air_quality.head


# In[185]:


air_quality_renamed = air_quality.rename(
columns ={"station_antwerp": "Lovergirl",
         "station_paris": "loverboy",
         "station_london": "Loverhi"})

air_quality_renamed.head()


# In[ ]:





# In[186]:


qf["Age"].mean()


# In[187]:


qf[["Age", "Fare"]]. median()


# In[188]:


qf[["Age", "Fare"]].describe()


# In[193]:


qf.agg({'Age': ['min', 'max', 'median', 'skew'],
             'Fare': ['min', 'max', 'median', 'skew']})


# In[196]:


qf[["Sex", "Age"]].groupby("Sex").mean()


# In[ ]:





# In[ ]:




