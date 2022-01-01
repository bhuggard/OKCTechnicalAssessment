#!/usr/bin/env python
# coding: utf-8

# In[179]:


import pandas as pd


# In[180]:


df = pd.read_csv("shots_data.csv")
df


# In[181]:


df['hypotenuse_sqd'] = (df['x'] * df['x']) + (df['y'] * df['y'])
df['abs'] = abs(df['x'])


# In[182]:


twopt1 = df.loc[(df['hypotenuse_sqd'] <= (23.75 * 23.75)) & (df['y'] > 7.8)]
twopt2 = df.loc[(df['abs'] <= 22) & (df['y'] <= 7.8)]


# In[183]:


twopt_final = pd.concat([twopt1,twopt2]).reset_index(drop=True)

twopt_final

# Did not drop duplicates as the same shot may have been attempted more than once, reset index to prevent gaps and errors in
# future work with the two point shot dataframe.


# In[184]:


corner_three = df.loc[(df['abs'] > 22) & (df['y'] <= 7.8)]

corner_three


# In[185]:


nc_three = df.loc[(df['hypotenuse_sqd'] > (23.75 * 23.75)) & (df['y'] > 7.8)]

nc_three             


# In[186]:


total_shots = len(df)
total_shots

# 560 Total Shots Taken


# In[187]:


a_shots = df.loc[df['team'] == "Team A"]
a_shots

# 280 Shots for Team A


# In[188]:


a_two_pt = twopt_final.loc[twopt_final['team'] == "Team A"]
print(len(a_two_pt))

#170/280 total shots for Team B were 2pt shots


# In[189]:


a_twopt_share =  (170/280)
a_twopt_share

# 60.71428571428571% of shots Team A took were 2pt shots


# In[190]:


a_corner_three = corner_three.loc[corner_three['team'] == "Team A"]

print(len(a_corner_three))

#20/280 total shots for Team A were corner 3pt shots


# In[191]:


a_corner_three_share =  (20/280)
a_corner_three_share

# 7.142857142857142% of shots Team A took were Corner Three Point shots


# In[192]:


a_nc_three = nc_three.loc[nc_three['team'] == "Team A"]
print(len(a_nc_three))

#90/280 total shots for Team A were Non-Corner 3pt Shots


# In[193]:


a_nc_three_share =  (90/280)
a_nc_three_share

# 32.142857142857146% of shots Team A took were Non-Corner Three Point shots


# In[194]:


b_shots = df.loc[df['team'] == "Team B"]
print(len(b_shots))

# 280 Shots for Team B


# In[195]:


b_two_pt = twopt_final.loc[twopt_final['team'] == "Team B"]
print(len(b_two_pt))

#163/280 total shots for Team B were 2pt shots


# In[196]:


b_twopt_share =  (163/280)
b_twopt_share

# 58.214285714285715% of shots Team B took were 2pt shots


# In[197]:


b_corner_three = corner_three.loc[corner_three['team'] == "Team B"]
print(len(b_corner_three))

#21/280 total shots for Team B were corner 3pt shots


# In[198]:


b_corner_three_share =  (21/280)
b_corner_three_share

# 7.5% of shots Team B took were Corner Three Point shots


# In[199]:


b_nc_three = nc_three.loc[nc_three['team'] == "Team B"]
print(len(b_nc_three))

#96/280 total shots for Team B were Non-Corner 3pt Shots


# In[200]:


b_nc_three_share =  (96/280)
b_nc_three_share

# 34.285714285714285% of shots Team B took were Non-Corner Three Point shots


# The following code relates to the EFG% Metrics from each zone for each team.

# In[201]:


# Team A


# In[202]:


a_two_pt_efg = sum(a_two_pt['fgmade']) / (len(a_two_pt))

a_two_pt_efg


# In[203]:


actm = sum(a_corner_three['fgmade'])

a_corner_three_efg = (actm + (0.5 * actm)) / (len(a_corner_three))

a_corner_three_efg


# In[204]:


anctm = sum(a_nc_three['fgmade'])
a_nc_three_efg = (anctm + (0.5 * anctm)) / (len(a_nc_three))

a_nc_three_efg


# In[205]:


# Team B


# In[206]:


b_two_pt_efg = sum(b_two_pt['fgmade']) / (len(b_two_pt))

b_two_pt_efg


# In[207]:


bctm = sum(b_corner_three['fgmade'])

b_corner_three_efg = (bctm + (0.5 * bctm)) / (len(b_corner_three))

b_corner_three_efg


# In[208]:


bnctm = sum(b_nc_three['fgmade'])
b_nc_three_efg = (bnctm + (0.5 * bnctm)) / (len(b_nc_three))

b_nc_three_efg

