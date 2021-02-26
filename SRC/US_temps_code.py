'''
*********************************************************************
imports
*********************************************************************
'''
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
'''
*********************************************************************
reading in file
*********************************************************************
'''

dfc= pd.read_csv('/Users/matiasgonzalez/Documents/dsi/Git/CapstoneI/Data/US_Temps_Final.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)

short_city = ['Colorado', 'California','New York', 'Florida', 'Texas', 'Alaska']

df_short_city = dfc[dfc['State'] == short_city]

us_1995_1 = df_short_city[(df_short_city["Year"] == 1995) & (df_short_city["Month"] == 1)& (df_short_city["State"] == short_city)]
print(us_1995_1)
