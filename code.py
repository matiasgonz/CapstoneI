'''
*********************************************************************
imports
*********************************************************************
'''
import pandas as pd
import plotly
from plotly import express
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
import seaborn as sns
import folium
'''
*********************************************************************
reading in file
*********************************************************************
'''

dfc= pd.read_csv('Data/US_Temps_Final.csv')
#pd.set_option("display.max_rows", None, "display.max_columns", None)
'''
# *********************************************************************
# data cleaning 
# *********************************************************************
# '''
# #select only entires in the  US
# df_US = dfc[(dfc.Country=='US')]
# #drop unneccessary columns 
# df1 = df_US.drop(columns=['Region', 'Country'])
# #drop incorrect numbers 
# drop_list = df1[df1.AvgTemperature  == -99].index
# df5 = df1.drop(drop_list, axis=0)
# #drop unneccesary years and 2020 due too incompletion
# df_US2 = df5.drop(df5[(df5['Year']==201) | (df5['Year']==200) | df5['Year']==2020].index)
# #drop additional terretories
# df4 = df_US2[~df_US2['State'].str.contains('Additional Territories')]
# df_US3 = df4.drop(df4[df4['City']=='Yuma'].index)
# #create a new csv
# df_US3.to_csv('Data/US_Temps_Final.csv', index = False)
'''
# *********************************************************************
# reimport file
# *********************************************************************
# '''
# df= pd.read_csv('Data/US_Temps.csv')
# '''
# *********************************************************************
# data exploration
# *********************************************************************
# '''
# #view complete data frame
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# #get info on dataframe
# print(df.info())
# #view first couple of lines
# print(df.head())
# #view full data frame
# print(df)
# #how many cities
# print(len(df.City.unique()))
# #look at data for one city
# print(df_month[df_month['City']=='Fairbanks'])
# '''
# *********************************************************************
# create a data frame for monthly avgs and yearly avgs
# *********************************************************************
# '''

# df_month = (
#        dfc.groupby(['State','City','Year','Month'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .sort_values(by=['State','City','Year','Month'])
#       )
# df_year = (
#        dfc.groupby(['State','City','Year'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .sort_values(by=['State','City','Year'])
#       )
# df_years = df_year.copy()
# df_city_temp = (
#        dfc.groupby(['City','Year'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .sort_values(by=['City','Year'])
#       )
# df_city = df_city_temp.copy()
# '''
# *********************************************************************
# t-test (with indepoendent t test)
# *********************************************************************
# '''
# df_temps_95_07 = df_city[df_city['Year'] < 2008]
# temps_95_07 = (
#        df_temps_95_07.groupby(['City'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .sort_values(by=['City'])
#       )
# temps_95 = temps_95_07.drop(columns=['City'])

# df_temps_07_19 = df_city[df_city['Year'] > 2008]
# temps_08_19 = (
#        df_temps_07_19.groupby(['City'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .sort_values(by=['City'])
#       )
# temps_19 = temps_08_19.drop(columns=['City'])

# ind_ttest = stats.ttest_ind(temps_95['AvgTemperature'], temps_19['AvgTemperature'])
# print(ind_ttest)

# '''
# # *********************************************************************
# # t-test (with Anova)
# # What type of statistical value do I get? The t-test and ANOVA produce a test statistic value (“t” or “F”, respectively), which is converted into a “p-value.” A p-value is the probability that the null hypothesis – that both (or all) populations are the same – is true. In other words, a lower p-value reflects a value that is more significantly different across populations. Biomarkers with significant differences between sample populations have p-values ≤ 0.05.
# # *********************************************************************
# '''
#avg of diff cities, over years
avg_temp_years = {}
for i in range(1995,2020):
    avg_temp_years[i] = dfc[dfc['Year'] == i]

df_data = {}
for i in range(1995,2020):
    df_data[i] = avg_temp_years[i].drop(columns=['City','Year'])

t_test = {}
for i in range(1995,2019):
    t_test[i] = stats.f_oneway(df_data[i]['AvgTemperature'], df_data[i+1]['AvgTemperature'])

t_test[2019] = stats.f_oneway(df_data[2018]['AvgTemperature'], df_data[2019]['AvgTemperature'])
t_test[2020] = stats.f_oneway(df_data[1995]['AvgTemperature'], df_data[2019]['AvgTemperature'])

# t_test_ex = t_test[i] = stats.f_oneway(df_data[1995]['AvgTemperature'], df_data[1996]['AvgTemperature'], df_data[1997]['AvgTemperature'],df_data[1998]['AvgTemperature'],df_data[1999]['AvgTemperature'],df_data[2000]['AvgTemperature'], df_data[2001]['AvgTemperature'],df_data[2002]['AvgTemperature'],df_data[2003]['AvgTemperature'],df_data[2004]['AvgTemperature'],df_data[2005]['AvgTemperature'],df_data[2006]['AvgTemperature'],df_data[2007]['AvgTemperature'],df_data[2008]['AvgTemperature'],df_data[2009]['AvgTemperature'],df_data[2010]['AvgTemperature'],df_data[2011]['AvgTemperature'],df_data[2012]['AvgTemperature'],df_data[2013]['AvgTemperature'],df_data[2014]['AvgTemperature'],df_data[2015]['AvgTemperature'],df_data[2016]['AvgTemperature'],df_data[2017]['AvgTemperature'],df_data[2018]['AvgTemperature'],df_data[2019]['AvgTemperature'])
# print (t_test_ex)

#print out dictionary with t test and final value being first year and last year 
for i in range(1995,2020):
    print (t_test[i])
'''
*********************************************************************
create pyplot with data overlaid on top of geographical map
*********************************************************************
'''
# df_temps_95 = dfc[dfc['Year'] == 2019]
# df_temps_19 = dfc[dfc['Year'] == 2019]

# df_plotly = (
#        dfc.groupby(['Year','State'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .rename(columns={'mean': 'AvgTemperature'})
#       .sort_values(by=['Year','State'])
#       )
# df_plotly_95 = (
#        df_temps_95.groupby(['Year','State'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .rename(columns={'mean': 'AvgTemperature'})
#       .sort_values(by=['Year','State'])
#       )
# df_plotly_19 = (
#        df_temps_19.groupby(['Year','State'])['AvgTemperature'].mean(['mean'])
#       .reset_index()
#       .rename(columns={'mean': 'AvgTemperature'})
#       .sort_values(by=['Year','State'])
#       )
# #df_plotly['Rank_hottest'] = df_plotly.groupby(by=['Year'])['AvgTemperature'].rank(method="min",ascending=False)
# #df_plotly['Rank_coldest'] = df_plotly.groupby(by=['Year'])['AvgTemperature'].rank(method="min",ascending=True)

# fig = (
#       express.choropleth(
#                  df_plotly2               
#                 ,locations='State'      
#                 ,color='AvgTemperature'
#                 ,animation_frame='Year'
#                 ,color_continuous_scale='Portland' 
#                 ,height=600
#                 ,scope='usa')
#   .update_layout(
#                  title_text='US AVERAGE TEMPERATURE'
#                 ,title_x=0.3
#                 ,margin=dict(r=10, t=40, b=10, l=10)
#                 ,coloraxis_colorbar_title='Temp °F')
    
# )
# fig.show()
'''
*********************************************************************
bar graphs
*********************************************************************
'''

# us_1995_1 = dfc[(dfc["Year"] == 1995) & (dfc["Month"] == 1)]
# plt.figure(figsize=(22,10))
# plt.title("The Average Temperature of States in the United States in 1995.")
# sns.barplot(x = us_1995_1["State"], y=us_1995_1["AvgTemperature"], data=us_1995_1)
# plt.xticks(rotation=90)

# us_2020_1 = dfc[(dfc["Year"] == 2020) & (dfc["Month"] == 1)]
# plt.figure(figsize=(22,10))
# plt.title("The Average Temperature of States in the United States in 2020.")
# sns.barplot(x = us_2020_1["State"], y=us_2020_1["AvgTemperature"], data=us_2020_1)
# plt.xticks(rotation=90)
# plt.show()
'''
*********************************************************************
folium
*********************************************************************
'''
# m = folium.Map(location=[37.6, -95.665])
# m.save(outfile='map.html')