#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd

df = pd.read_csv("report2.csv")

df.set_index("WeekNumb", inplace=True)

responsetime = df["response_time_comment"] / 3600


finaltime = responsetime.groupby(['WeekNumb']).mean().dropna()

print((finaltime/8)) # print average number of days it took for first response

ax = (finaltime/8).plot(x = 'WeekNumb', y= 'Average days')

ax.set_xlim((23,53))

ax.set_ylim((0,10))

ax.set_ylabel("Average First Response (Hours)")



# In[ ]:




