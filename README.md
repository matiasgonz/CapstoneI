# Is Climate Change real?

<p align="center">
  <img src="/Users/matiasgonzalez/Documents/dsi/Git/CapstoneI/Images.ClimateChange.jpg" width = 900 height = 60>
</p>


*Capstone I Project for Galvanize Data Science Immersive*

*by Matias Gonzalez*


## Table of Contents
- [Introduction](#introduction)
  - [Background](#background)
  - [The Data](#the-data)
  - [Question and Hypothesis](#question-and-hypothesis)
- [Exploratory Data Analysis and Data Cleaning](#exploratory-data-analysis-and-Data-Cleaning)
- [Data Visulization](#Data-Visualization)
  - [Barplots](#barplots)
  - [Heat Map](#Heat_map)
- [T-Test](#T-Test)
  - [ANOVA (Analysis of Variance)](#ANOVA-(Analysis-of-Variance))
  - [Model Assessment](#model-assessment)
  - [Results and Interpretation](#results-and-interpretation)
- [Conclusion](#Conclusion)

# Introduction

## Background
There are houndreads if not thousands of published studies proving Climate Change and Globa Warming. Some use surface temperatures, other look at ozone layers, and some even look at sea levels. All of these grand studies defintly prove Climate Change but it is hard to find one that is simple and straight to the point. 

The goal of this project is to demonstrate the changes in temperatue over a period of time and determine with statistical certenty wether these values are significantly diffrent. 

## The Data
The University of Dayton published a CSV file in 2020 containing the average daily temperatures of over 320 cities from 1995 to 2020. The data set contains weather, more precisly average daily temperature in Farenheit, of 157 US cities and 167 international cities.

## Question and Hypothesis
We are going to try to demonstrate the effect of Climate Change by showing the change in temperature over a period of time. We are going to statistically prove that this change has been significant over the time period. We are going to cut donw the data set ot only include US cities in order to make our study more digestable.

Can we demonstarte that there has been a significant change in temperature over the years?
We are going to use an ANOVA (Analysis of Variance) T-Test to statistically proof the variance between diffrent years.

[Back to Top](#Table-of-Contents)

# Exploratory Data Analysis and Data Cleaning
So first we get the general info and a look at the data.
<p align="center">
  <img src="images/math_pairplot.png" width = 400>
  <img src="images/port_pairplot.png" width = 400>
</p>
We can see from this initial exploration that there are 8 columns to describe the data and we have around 3 million entries. 

Since we are only going to be working with US cities we want to exlude all non US cities from our data. Since we were also able to see that some terretories are included we will also be droppping those. We will also be dropping all values set to -99 since those are used as placeholders for invalid data.  

After we have filtered out our data for all unnecessary cities we take a look at the data again. We will extract our unique cities inside the data. We are also going to take an overall look at these cities in order to make sure we have the correct data. 

After dropping some cities which had incomplete data we can see these are the cities we are working with. We also had to drop the year 2020 from the study since it was incomplete. Further data cleaning was done with min and max to identiify outliers. 

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

After confirming we have the right data selection and cleaned all of our data we can drop unneccesary columns. (Region and country) an this is how the dataframe we will be working with looks like. 

<p align="center">
  <img src="images/m_g3_dist.png" width = 400>
  <img src="images/p_g3_dist.png" width = 400>
</p>


[Back to Top](#Table-of-Contents)

# Data Visualization

## Barplots
<p align="center">
  <img src="images/m_g3_dist.png" width = 400>
  <img src="images/p_g3_dist.png" width = 400>
</p>

## Heat map

[Back to Top](#Table-of-Contents)

# T-Test
A T-test is a statistical test used to determine if there is a significance change in mean in data. It is used as a hypothesis testing tool that allows testing of an assumption applicable to a population. T-test are used to determine statistical significance. We are going to be using a T-test in order to demonstrate there has been significant change in temperature over a period of time. There are many diffrent types of T-Test. We are going to be concentrating on the ANOVA test

## ANOVA (Analysis of Variance)
The t-test and ANOVA produce a test statistic value (“t” or “F”, respectively), which is converted into a “p-value.” A p-value is the probability that the null hypothesis is true. In other words, a lower p-value reflects a value that is more significantly different across populations.

## Results and Interpretation
Our result when preforming an ANOVA T-test are as follows. 

F_onewayResult(statistic=4.8186759678453335, pvalue=0.028155013645666947)

As we can see form out results our pvalue is pretty low, it being 0.028. Like stated above the smaller our pvalue is the greater chance to prove our null hypothesis. In this case since it is so low we will accept our hypothesis and we can safely say that there is a significant change in the values of our variables. 

[Back to Top](#Table-of-Contents)

# Conclusion


[Back to Top](#Table-of-Contents)