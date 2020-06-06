#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Importing Python libraries

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


# In[2]:


## loading dataset and creating, making adjustments to dataframe.

df = pd.read_excel('Master v4.xlsx')
df = df.fillna(0)
df['Date'] = pd.to_datetime(df['Date'])
mask = (df['Date'] > '2020-01-22') & (df['Date'] <= '2020-06-02')
df.loc[mask]
df['Deaths'] = df['Deaths'].astype(int)
df['Confirmed Cases'] = df['Confirmed Cases'].astype(int)
df['Recovered'] = df['Recovered'].astype(int)
df['Daily Confirmed'] = df['Daily Confirmed'].astype(int)
df['Country'] = df['Country'].astype(str)

df.head()


# In[3]:


##Creating a dataframe for mapping filtered data (date)

Daily_Confirmed_Cases = df[['Country', 'Daily Confirmed', 'Date', 'CODE']]
data_for_map = Daily_Confirmed_Cases[Daily_Confirmed_Cases['Date']=='2020-06-02']
data_for_map.head(200)

##Visualizing filtered data in a simple map.

fig = px.choropleth(data_for_map, locations="CODE", color="Daily Confirmed",
                    color_continuous_scale=[(0, "lightgrey"), (0.075, "purple"), (0.15, "brown"), (0.575, "orange"), (1, "red")])

fig.show()


# In[4]:


##Creating a Datatable for visualzing filtered data. (Date)

Datatable = df[['Country', 'Date', 'Daily Confirmed', 'Confirmed Cases', 'Daily Deaths', 'Deaths', 'Daily Recovered', 'Recovered']]
Data_datatable = Datatable[df['Date']=='2020-06-02']
Data_datatable = Data_datatable.sort_values(['Daily Confirmed'], ascending=False)
Data_datatable.head(200)


# In[5]:


## Creating a dataframe for Graphing filtered data. (Cumulative Deaths)

CumDeaths = df[['Country', 'Date', 'Daily Confirmed', 'Deaths']]
CumDeaths = CumDeaths[df['Date']=='2020-06-02'] 
CumDeaths = CumDeaths[df['Deaths']>=5000]
CumDeaths = CumDeaths[['Country', 'Deaths']]
CumDeaths = CumDeaths.sort_values(['Deaths'], ascending=True)
CumDeaths.head(20)

## Visualizing the dataframe in bar graph. 

fig = plt.barh(CumDeaths.Country, CumDeaths.Deaths)
ax1 = plt.subplot(111)
ret = ax1.barh(CumDeaths['Country'], CumDeaths['Deaths'],color = '#ff8803')
ax1.xaxis.grid(linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(CumDeaths.Deaths):
    ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, CumDeaths.Deaths.max() * 1.3)


# In[6]:


## Creating a dataframe for Graphing filtered data. (Cumulative Recovered)

CumRecovered = df[['Country', 'Date', 'Daily Confirmed', 'Recovered']]
CumRecovered = CumRecovered[df['Date']=='2020-06-02'] 
CumRecovered = CumRecovered[df['Recovered']>=50000]
CumRecovered = CumRecovered[['Country', 'Recovered']]
CumRecovered = CumRecovered.sort_values(['Recovered'])
CumRecovered.head(30)

## Visualizing the dataframe in bar graph.

fig = plt.barh(CumRecovered.Country, CumRecovered.Recovered)
ax1 = plt.subplot(111)
ret = ax1.barh(CumRecovered['Country'], CumRecovered['Recovered'],color = '#ff8803')
ax1.xaxis.grid(linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(CumRecovered.Recovered):
    ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, CumRecovered.Recovered.max() * 1.3)  


# In[7]:


## Creating a dataframe for Graphing filtered data. (Daily Confirmed)

DailyCC = df[['Country', 'Date', 'Daily Confirmed']]
DailyCC = DailyCC[df['Date']=='2020-06-02'] 
DailyCC = DailyCC[df['Daily Confirmed']>=1250]
DailyCC = DailyCC[['Country', 'Daily Confirmed']]
DailyCC = DailyCC.sort_values(['Daily Confirmed'])
DailyCC.columns = ['Country', 'Daily_Confirmed']
DailyCC.head(200)

## Visualizing the dataframe in bar graph.

fig = plt.barh(DailyCC.Country, DailyCC.Daily_Confirmed)
ax1 = plt.subplot(111)
ret = ax1.barh(DailyCC['Country'], DailyCC['Daily_Confirmed'],color = '#ff8803')
ax1.xaxis.grid(linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(DailyCC.Daily_Confirmed):
    ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, DailyCC.Daily_Confirmed.max() * 1.3)  


# In[8]:


## Creating a dataframe for Graphing filtered data. (Daily Confirmed)

CumCases = df[['Country', 'Date', 'Daily Confirmed', 'Confirmed Cases']]
CumCases = CumCases[df['Date']=='2020-06-02'] 
CumCases = CumCases[df['Confirmed Cases']>=150000]
CumCases = CumCases[['Country', 'Confirmed Cases']]
CumCases = CumCases.sort_values(['Confirmed Cases'])
CumCases.columns = ['Country', 'Confirmed_Cases']
CumCases.head(200)

## Visualizing the dataframe in bar graph.

fig = plt.barh(CumCases.Country, CumCases.Confirmed_Cases)
ax1 = plt.subplot(111)
CumCases.sort_values('Confirmed_Cases', inplace=True)
ret = ax1.barh(CumCases['Country'], CumCases['Confirmed_Cases'],color = '#ff8803')
ax1.xaxis.grid(linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(CumCases.Confirmed_Cases):
    ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, CumCases.Confirmed_Cases.max() * 1.3)  


# In[9]:


## Creating a dataframe for Graphing filtered data. (Daily Deaths)

DailyDeaths = df[['Country', 'Date', 'Daily Deaths']]
DailyDeaths = DailyDeaths[df['Date']=='2020-06-02'] 
DailyDeaths = DailyDeaths[df['Daily Deaths']>=75]
DailyDeaths = DailyDeaths[['Country', 'Daily Deaths']]
DailyDeaths = DailyDeaths.sort_values(['Daily Deaths'])
DailyDeaths.columns = ['Country', 'Daily_Deaths']
DailyDeaths.head(30)

## Visualizing the dataframe in bar graph.

fig = plt.barh(DailyDeaths.Country, DailyDeaths.Daily_Deaths)
ax1 = plt.subplot(111)
DailyDeaths.sort_values('Daily_Deaths', inplace=True)
ret = ax1.barh(DailyDeaths['Country'], DailyDeaths['Daily_Deaths'],color = '#ff8803')
ax1.xaxis.grid(linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(DailyDeaths.Daily_Deaths):
    ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, DailyDeaths.Daily_Deaths.max() * 1.3) 


# In[10]:


## Creating a dataframe for Graphing filtered data. (Daily Recovered)

DRecovered = df[['Country', 'Date', 'Daily Recovered']]
DRecovered = DRecovered[df['Date']=='2020-06-02'] 
DRecovered = DRecovered[df['Daily Recovered']>=750]
DRecovered = DRecovered[['Country', 'Daily Recovered']]
DRecovered = DRecovered.sort_values(['Daily Recovered'])
DRecovered.columns = ['Country', 'Daily_Recovered']
DRecovered.head(30)

## Visualizing the dataframe in bar graph.

fig = plt.barh(DRecovered.Country, DRecovered.Daily_Recovered)
ax1 = plt.subplot(111)
ret = ax1.barh(DRecovered['Country'], DRecovered['Daily_Recovered'],color = '#ff8803',linestyle = '--', linewidth = 0.5)
for pY, pX in enumerate(DRecovered.Daily_Recovered):
        ax1.annotate("{:,}".format(pX), xy=(pX, pY), fontstyle = 'italic', va = 'center' , fontsize = 11)
ax1.set_xlim(0, DRecovered.Daily_Recovered.max() * 1.3) 


# In[11]:


## Creating a dataframe for Graphing filtered data. (Region; Latin America & Caribbean)

RCases_SA = df[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_SA = RCases_SA[(df['Date'] > '2020-02-22') & (df['Date'] <= '2020-06-02')]
RCases_SA = RCases_SA[df['Confirmed Cases']>=10000]
RCases_SA = RCases_SA[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_SA = RCases_SA[df['Region']=="Latin America & Caribbean"]
RCases_SA.columns = ['Country', 'Date', 'Confirmed_Cases', 'Region']
RCases_SA = RCases_SA.sort_values(['Date'])
RCases_SA.head(200)

## Visualizing the dataframe in a comparative line graph (Logarithmic scale).

df2 = RCases_SA
df2['Confirmed_Cases'] = df2['Confirmed_Cases'].astype(int)
fig = px.line(df2, x="Date", y="Confirmed_Cases", color='Country')
fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=500,
    width=500,
    title_text='Latin America & Caribbean'
)
 
    
fig.show()


# In[12]:


## Creating a dataframe for Graphing filtered data. (Region; Europe)

RCases_EU = df[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_EU = RCases_EU[(df['Date'] > '2020-02-22') & (df['Date'] <= '2020-05-31')]
RCases_EU = RCases_EU[df['Confirmed Cases']>=10000]
RCases_EU = RCases_EU[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_EU = RCases_EU[df['Region']=="Europe"]
RCases_EU.columns = ['Country', 'Date', 'Confirmed_Cases', 'Region']
RCases_EU = RCases_EU.sort_values(['Date'])
RCases_EU.head(200)

## Visualizing the dataframe in a comparative line graph. (Logarithmic scale)

df2 = RCases_EU
df2['Confirmed_Cases'] = df2['Confirmed_Cases'].astype(int)
fig = px.line(df2, x="Date", y="Confirmed_Cases", color='Country')
fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=500,
    width=500,
    title_text='Europe'
)
 
    
fig.show()


# In[13]:


## Creating a dataframe for Graphing filtered data. (Countries with over 100,000 Cumulative Cases)

CCases_LG = df[['Country', 'Date', 'Confirmed Cases','Region']]
CCases_LG = CCases_LG[(df['Date'] > '2020-02-22') & (df['Date'] <= '2020-06-02')]
CCases_LG = CCases_LG[df['Confirmed Cases']>=100000]
CCases_LG = CCases_LG[['Country', 'Date', 'Confirmed Cases','Region']]
CCases_LG.columns = ['Country', 'Date', 'Confirmed_Cases', 'Region']
CCases_LG = CCases_LG.sort_values(['Date'])
CCases_LG.head(200)

## Visualizing the dataframe in a comparative line graph (Logarithmic scale).

df2 = CCases_LG
fig = px.line(df2, x="Date", y="Confirmed_Cases", color='Country')
fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=500,
    width=500,
    title_text='GLobal Cumulative Cases'
)
 
    
fig.show()


# In[14]:


## Creating a dataframe for Graphing filtered data. (Region; Middle East & North Africa)

RCases_MENA = df[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_MENA = RCases_MENA[(df['Date'] > '2020-02-22') & (df['Date'] <= '2020-05-31')]
RCases_MENA = RCases_MENA[df['Confirmed Cases']>=20000]
RCases_MENA = RCases_MENA[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_MENA = RCases_MENA[df['Region']=="Middle East & North Africa"]
RCases_MENA.columns = ['Country', 'Date', 'Confirmed_Cases', 'Region']
RCases_MENA = RCases_MENA.sort_values(['Date'])
RCases_MENA.head(200)

## Visualizing the dataframe in a comparative line graph. (Logarithmic scale)

df2 = RCases_MENA
df2['Confirmed_Cases'] = df2['Confirmed_Cases'].astype(int)
fig = px.line(df2, x="Date", y="Confirmed_Cases", color='Country')
fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=500,
    width=500,
    title_text='Middle East & North Africa'
)
    
fig.show()


# In[15]:


## Creating a dataframe for Graphing filtered data. (Region; Central Asia)

RCases_CA = df[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_CA = RCases_CA[(df['Date'] > '2020-02-22') & (df['Date'] <= '2020-05-31')]
RCases_CA = RCases_CA[df['Confirmed Cases']>=1000]
RCases_CA = RCases_CA[['Country', 'Date', 'Confirmed Cases', 'Region']]
RCases_CA = RCases_CA[df['Region']=="Central Asia"]
RCases_CA.columns = ['Country', 'Date', 'Confirmed_Cases', 'Region']
RCases_CA = RCases_CA.sort_values(['Date'])
RCases_CA.head(200)

## Visualizing the dataframe in a comparative line graph. (Logarithmic scale)

df2 = RCases_CA
df2['Confirmed_Cases'] = df2['Confirmed_Cases'].astype(int)
fig = px.line(df2, x="Date", y="Confirmed_Cases", color='Country')
fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_traces(textposition='top center')

fig.update_layout(
    height=500,
    width=500,
    title_text='Central Asia'
)
    
fig.show()


# In[16]:


for template in ["plotly_dark"]:
    fig = px.scatter(RCases_CA,
                     x="Date", y="Confirmed_Cases", color="Country",
                     log_x=True, size_max=60,
                     template=template, title="Central Asia")

fig.update_layout(xaxis_type="date", yaxis_type="log")

fig.update_layout(
    height=500,
    width=600,
)
    
fig.show()
    

