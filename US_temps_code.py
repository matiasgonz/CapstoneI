'''
*********************************************************************
imports
*********************************************************************
'''
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
'''
*********************************************************************
reading in file
*********************************************************************
'''

dfc= pd.read_csv('Data/US_temps5.csv')
pd.set_option("display.max_rows", None, "display.max_columns", None)

'''
*********************************************************************
data cleaning 
since its world data drop all other countries
drop additional terretories (Puerto Rico)
drop incorrect numbers 
create a new csv
*********************************************************************
'''

cities = ['Birmingham', 'Huntsville', 'Mobile', 'Montgomery', 'Anchorage',
       'Fairbanks', 'Juneau', 'Flagstaff', 'Phoenix', 'Tucson', 'Yuma',
       'Fort Smith', 'Little Rock', 'Fresno', 'Los Angeles', 'Sacramento',
       'San Diego', 'San Francisco', 'Colorado Springs', 'Denver',
       'Grand Junction', 'Pueblo', 'Bridgeport', 'Hartford Springfield',
       'Wilmington', 'Washington', 'Daytona Beach', 'Jacksonville',
       'Miami Beach', 'Orlando', 'Tallahassee', 'Tampa St. Petersburg',
       'West Palm Beach', 'Atlanta', 'Columbus', 'Macon', 'Savannah',
       'Honolulu', 'Boise', 'Pocatello', 'Chicago', 'Peoria', 'Rockford',
       'Springfield', 'Evansville', 'Fort Wayne', 'Indianapolis',
       'South Bend', 'Des Moines', 'Sioux City', 'Goodland', 'Topeka',
       'Wichita', 'Lexington', 'Louisville', 'Paducah', 'Baton Rouge',
       'Lake Charles', 'New Orleans', 'Shreveport', 'Caribou', 'Portland',
       'Baltimore', 'Washington DC', 'Boston', 'Detroit', 'Flint',
       'Grand Rapids', 'Lansing', 'Sault Ste Marie', 'Duluth',
       'Minneapolis St. Paul', 'Jackson', 'Tupelo', 'Kansas City',
       'St Louis', 'Billings', 'Great Falls', 'Helena', 'Lincoln',
       'North Platte', 'Omaha', 'Las Vegas', 'Reno', 'Concord',
       'Atlantic City', 'Newark', 'Albuquerque', 'Albany', 'Buffalo',
       'New York City', 'Rochester', 'Syracuse', 'Asheville', 'Charlotte',
       'Greensboro', 'Raleigh Durham', 'Bismarck', 'Fargo',
       'Akron Canton', 'Cincinnati', 'Cleveland', 'Dayton', 'Toledo',
       'Youngstown', 'Oklahoma City', 'Tulsa', 'Eugene', 'Medford',
       'Salem', 'Allentown', 'Erie', 'Harrisburg', 'Philadelphia',
       'Pittsburgh', 'Wilkes Barre', 'Rhode Island', 'Charleston',
       'Columbia', 'Rapid City', 'Sioux Falls', 'Chattanooga',
       'Knoxville', 'Memphis', 'Nashville', 'Abilene', 'Amarillo',
       'Austin', 'Brownsville', 'Corpus Christi', 'Dallas Ft Worth',
       'El Paso', 'Houston', 'Lubbock', 'Midland Odessa', 'San Angelo',
       'San Antonio', 'Waco', 'Wichita Falls', 'Salt Lake City',
       'Burlington', 'Norfolk', 'Richmond', 'Roanoke', 'Seattle',
       'Spokane', 'Yakima', 'Elkins', 'Green Bay', 'Madison', 'Milwaukee',
       'Casper', 'Cheyenne']

# print(df.info())
# x = df.drop(columns=['Region', 'Country'])
# y = df.drop(df.State == 'Additional Territories')
# df[df.State == 'Additional Territories']
# new_df = df[~df['State'].str.contains('Additional Territories')]
# print(new_df)
# new_df.to_csv('Data/US_temps4.csv', index = False)
# print(len(df.City.unique()))

# print(df_month[df_month['City']=='Fairbanks'])
# drop_list = df[df.AvgTemperature  == -99].index
# df2 = df.drop(drop_list, axis=0)
# df2.to_csv('Data/US_temps5.csv', index = False)
# df = pd.read_csv('Data/city_temperature.csv')
# df_US = df[(df.Country=='US')]
# df_US.to_csv('Data/US_temps2.csv', index = False)
dfa = df.drop(df[(df['Year']==201) | (df['Year']==200) | df['Year']==2020].index)
dfc = dfa.drop(dfa[dfa['City']=='Yuma'].index)

dfc.to_csv('Data/US_Temps.csv', index = False)

'''
*********************************************************************
create a data frame for monthly avgs and yearly avgs
*********************************************************************
'''

df_month = (
       dfc.groupby(['State','City','Year','Month'])['AvgTemperature'].mean(['mean'])
      .reset_index()
      .sort_values(by=['State','City','Year','Month'])
      )
df_year = (
       dfc.groupby(['State','City','Year'])['AvgTemperature'].mean(['mean'])
      .reset_index()
      .sort_values(by=['State','City','Year'])
      )
df_years = df_year.copy()
df_city_temp = (
       dfc.groupby(['City','Year'])['AvgTemperature'].mean(['mean'])
      .reset_index()
      .sort_values(by=['City','Year'])
      )
df_city = df_city_temp.copy()

'''
*********************************************************************
t-test (with indepoendent t test)
*********************************************************************
'''
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

'''
*********************************************************************
t-test (with Anova)
*********************************************************************
'''
""" #avg of diff cities, over years
avg_temp_years = {}
for i in range(1995,2020):
    avg_temp_years[i] = df_city[df_city['Year'] == i]

df_data = {}
for i in range(1995,2020):
    df_data[i] = avg_temp_years[i].drop(columns=['City','Year'])

#print(df_data_1995)
t_test = {}
for i in range(1995,2019):
    t_test[i] = stats.f_oneway(df_data[i]['AvgTemperature'], df_data[i+1]['AvgTemperature'])

t_test[2019] = stats.f_oneway(df_data[2018]['AvgTemperature'], df_data[2019]['AvgTemperature'])
t_test[2020] = stats.f_oneway(df_data[1995]['AvgTemperature'], df_data[2019]['AvgTemperature'])

t_test_ex = t_test[i] = f_oneway(df_data[1995]['AvgTemperature'], df_data[1996]['AvgTemperature'], df_data[1997]['AvgTemperature'],df_data[1998]['AvgTemperature'],df_data[1999]['AvgTemperature'],df_data[2000]['AvgTemperature'], df_data[2001]['AvgTemperature'],df_data[2002]['AvgTemperature'],df_data[2003]['AvgTemperature'],df_data[2004]['AvgTemperature'],df_data[2005]['AvgTemperature'],df_data[2006]['AvgTemperature'],df_data[2007]['AvgTemperature'],df_data[2008]['AvgTemperature'],df_data[2009]['AvgTemperature'],df_data[2010]['AvgTemperature'],df_data[2011]['AvgTemperature'],df_data[2012]['AvgTemperature'],df_data[2013]['AvgTemperature'],df_data[2014]['AvgTemperature'],df_data[2015]['AvgTemperature'],df_data[2016]['AvgTemperature'],df_data[2017]['AvgTemperature'],df_data[2018]['AvgTemperature'],df_data[2019]['AvgTemperature'])
print (t_test_ex)

#print out dictionary with t test and final value being first year and last year 
#for i in range(1995,2020):
    #print (t_test[i]) """

'''
*********************************************************************
pivot table of rate of temperature
*********************************************************************
Average Temperature variation over the years
pd.pivot_table(dfc,index=['Year'],values=['AvgTemperature'],aggfunc=np.mean).plot(kind='line',color='orange')
plt.title("Average Temperature variation over the years", loc='center', fontsize=12, fontweight=0, color='orange')
plt.xlabel("Year")
plt.ylabel("Average Temperature")

plt.show()
'''
'''
*********************************************************************
barplot of change of
*********************************************************************
'''

'''
*********************************************************************
boxchart
*********************************************************************

avg_temperature={}
keys=list(df_year['City'].unique())
for city in keys:
    avg_temperature['City']=df_copy[(df_copy['City']==cities)&(df_copy['Year']==2020)]['AvgTemperature'].mean()-df_copy[(df_copy['City']==cities)&(df_copy['Year']==1995)]['AvgTemperature']
avg_temperature_rise=pd.DataFrame(list(avg_temperature.items()),columns=['City','Average Temperature rise'])

sns.barplot(x='Average Temperature rise',y='City',data=avg_temperature_rise.sort_values(by='Average Temperature rise',ascending=False, axis=1)).set_title('Increase in Average Temperature by Region')
'''
'''
*********************************************************************
boxchart of tempertue divided by state
*********************************************************************

# Loop through each region and plot average temperature
plt.figure(figsize=(153,7.5)
for city in cities:
    temp = dfc[dfc['City'].unique()== cities]
    temp = temp.groupby("Year")["AvgTemperature"].mean()
    a = temp
    plt.plot(a)
    
plt.legend(cities, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.title('Average Annual Temperature by RegCityion')
plt.xlabel('Year')
plt.ylabel('Average Temperature, Fahrenheit')

plt.show()
'''

'''
*********************************************************************
create pyplot with data overlaid on top of geographical map
*********************************************************************
'''
# Create a grid : initialize it
g = sns.FacetGrid(dfc, col='', hue='country', col_wrap=4, )
 
# Add the line over the area with the plot function
g = g.map(plt.plot, 'years', 'value')
 
# Fill the area with fill_between
g = g.map(plt.fill_between, 'years', 'value', alpha=0.2).set_titles("{col_name} country")
 
# Control the title of each facet
g = g.set_titles("{col_name}")
 
# Add a title for the whole plo
plt.subplots_adjust(top=0.92)
g = g.fig.suptitle('Evolution of the value of stuff in 16 countries')
 
plot.show()

print(dfc.groupby(by=['Year'])['AvgTemperature'].rank(method="min",ascending=False))
print(dfc.groupby(by=['Year'])['AvgTemperature'].rank(method="min",ascending=True))

US overlay Map
fig = (
   px.choropleth(
                 dfc               
                ,locations='City'               
                ,color='AvgTemperature'
                ,hover_name='City'  
                ,animation_frame='Year'
                ,color_continuous_scale='Portland' 
                ,height=600)
  .update_layout(
                 title_text='US AVERAGE TEMPERATURE'
                ,title_x=0.3
                ,margin=dict(r=10, t=40, b=10, l=10)
                ,coloraxis_colorbar_title='Temp °C')
    .update_geos(
                visible=False, resolution=110, scope="usa",
                showcountries=True, countrycolor="Black",
                showsubunits=True, subunitcolor="Blue"
)
)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 800
fig.show()

State Abbreviation	FIPS Code	State Name	State Abbreviation	FIPS Code	State Name
AK	02	ALASKA	MS	28	MISSISSIPPI
AL	01	ALABAMA	MT	30	MONTANA
AR	05	ARKANSAS	NC	37	NORTH CAROLINA
AS	60	AMERICAN SAMOA	ND	38	NORTH DAKOTA
AZ	04	ARIZONA	NE	31	NEBRASKA
CA	06	CALIFORNIA	NH	33	NEW HAMPSHIRE
CO	08	COLORADO	NJ	34	NEW JERSEY
CT	09	CONNECTICUT	NM	35	NEW MEXICO
DC	11	DISTRICT OF COLUMBIA	NV	32	NEVADA
DE	10	DELAWARE	NY	36	NEW YORK
FL	12	FLORIDA	OH	39	OHIO
GA	13	GEORGIA	OK	40	OKLAHOMA
GU	66	GUAM	OR	41	OREGON
HI	15	HAWAII	PA	42	PENNSYLVANIA
IA	19	IOWA	PR	72	PUERTO RICO
ID	16	IDAHO	RI	44	RHODE ISLAND
IL	17	ILLINOIS	SC	45	SOUTH CAROLINA
IN	18	INDIANA	SD	46	SOUTH DAKOTA
KS	20	KANSAS	TN	47	TENNESSEE
KY	21	KENTUCKY	TX	48	TEXAS
LA	22	LOUISIANA	UT	49	UTAH
MA	25	MASSACHUSETTS	VA	51	VIRGINIA
MD	24	MARYLAND	VI	78	VIRGIN ISLANDS
ME	23	MAINE	VT	50	VERMONT
MI	26	MICHIGAN	WA	53	WASHINGTON
MN	27	MINNESOTA	WI	55	WISCONSIN
MO	29	MISSOURI	WV	54	WEST VIRGINIA
 	 	 	WY	56	WYOMING

