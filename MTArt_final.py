
# coding: utf-8

# # MTArt 
# ### Exploratory Data Analysis & Visualization- Final project
# Julien Maudet & Franck Ngamkan
# 
# ###### Link to the source code https://github.com/julmaud/MTArt
# 
# ### Which NYC subway station should an emerging artist eager to share his work go to?
# <br>
# <br>
# 
# ## Motivation
# First look at this video of Oriel Ceballos selling art in the subway:
# 
# <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:28.125% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BS6h03Pgdfb/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">A video of my #subway #gallery. FYI: Come see my Poetic Justice Exhibit this Monday, April 17th from 7pm-10pm @daddygreenspizzabk 352 Malcolm X BLVD, Brooklyn, NY 11233. I am the curator for this  amazing exhibition, which will feature talented artists, musicians, and poets. Hope to see you there. #or1el#artist#nyc#nycsubway#nycartist#nycblogger#nycart#nyc❤️#nyctattoo#nyclife#nycphotography#subwayart#subwaysketch#subwaypeople#artwork#artfido#art#artlife#artstudio</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">Une publication partagée par Oriel Ceballos (@or1el) le <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2017-04-15T17:32:52+00:00">15 Avril 2017 à 10h32 PDT</time></p></div></blockquote>
# <script async defer src="http://platform.instagram.com/en_US/embeds.js"></script>
# 
# and this photo:
# 
# <blockquote class="instagram-media" data-instgrm-captioned data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div> <p style=" margin:8px 0 0 0; padding:0 4px;"> <a href="https://www.instagram.com/p/BSlnTSygktZ/" style=" color:#000; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none; word-wrap:break-word;" target="_blank">My original #GetOut 5&#34;x7 painting was pricey, but after watching the movie, this young queen was compelled to buy it. I was happy to learn that it&#39;s a birthday gift for her cousin who loves art. We&#39;ve got good people out here! I&#39;m glad we met. Follow @or1el for more #dopeness and to attend my forthcoming Poetic Justice Exhibit on April 17th from 7pm-10pm @daddygreenspizzabk. 🎨👑✈️️</a></p> <p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;">Une publication partagée par Oriel Ceballos (@or1el) le <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2017-04-07T14:36:40+00:00">7 Avril 2017 à 7h36 PDT</time></p></div></blockquote>
# <script async defer src="http://platform.instagram.com/en_US/embeds.js"></script>
# 
# ### Context and Inspiration
# 
# We had the idea of conducting such a project, that can sound a bit original in the beginning, when we met Oriel Ceballos at an art show in Harlem earlier this year. After a successful career as a professor, he decided to take an early exit and started a life as a full time artist, collector and curator. More info on him can be found on his Instagram page: https://www.instagram.com/or1el/?hl=fr
# 
# In order to broaden his audience, engage to people and sell his artworks, Oriel regularly - several days per week - go to a subway station in either Manhattan or Brooklyn, displays his artworks and paints live, while engaging with commuters.
# 
# Concerning his station selection process, he would just try stations with traffic and where he would have enough space to display his artworks. However, it rang a bell in our data science-sensitized ears. 
# 
# Let's gather data about subway stations that are relevant to our use case and try to come out with a way for artists to optimally select the subway station that best suits their requirements!!
# 
# ### How to make it into a Data visualization use case? 
# 
# In order to go from our envy and inspiration to a data visualization task, we needed to gather datasets. But before gathering datasets, we needed to know what kind of data we were looking for. In particular, what features of subway stations were relevant to our analysis.
# 
# Here are our hypothesis on the features that matter:
#     
#     Is there a lot of traffic in the station?
#     How easy and convenient is the access to the station?
#     Are the people commuting here interested in Art? 
#     Are they wealthy?
#     
# We are not stating that the best station is the station with most traffic, in a very arty place, and with very reach people. The point here is to be able to discuss those variables in order to find the best match between an artist and a subway station.
# 
# ## Data Sources
# 
# We got our data from different sources: MTA turnstile data, NYC Open Data platform, and by crunching some information manually.
# 
# ### Open Data
#     
# #### Traffic data
# In this task, We started from the great work by Henri Dwyer, that can be found here: https://henri.io/posts/new-york-subway-traffic-data-part-1.html. The original data is here: http://web.mta.info/developers/turnstile.html
# 
# In its final format, for each subway station, it includes the mean daily traffic, as well as the daily traffic for 6 consecutive days in April 2017.
# 
# #### Art galleries
# In order to link a subway station with an appeal for art, we decided to count the number of art galleries in a radius of 0.2 miles around the subway station. This would be a great indicator of the appeal for art in the zone.
# 
# We found the data to do so on NYC OpenData: https://data.cityofnewyork.us/Recreation/New-York-City-Art-Galleries/tgyc-r5jh/data
# 
# The dataset includes all art galleries in New York, many information on the galleries such as name, telephone.. and the GPS coordinates.
#     
# #### Details of subway stations
# For each station, we needed the GPS coordinates, to link them to the art galleries and the neighborhood, the name of the station and the type of Entrance.
# 
# We found these information on NYC OpenData: https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49/data
# 
# 
# ### Manual Data collection
# 
# #### NYC Neighborhoods : Median income & coordinates
# In order to have insights on the wealth of commuters at each station, one indicator is the median income in the neighborhood of the station.
# We found this information on this website: http://statisticalatlas.com/county-subdivision/New-York/New-York-County/Manhattan/Household-Income#figure/neighborhood and scrapped manually. 
# 
# We then collected the GPS coordinates of the centroid of each neighborhood using Google Maps, in order to link each station to the neighborhood of the centroid it is the closest to. 
# 
# 
# ## Data Preprocessing
# 
# ### Data Preparation
# 
# We have had to proceed to the following preprocessing steps:
#     
#     Prepare all GPS coordinates to the same format
#     Transform the traffic data in a usable format. From turnstile events to daily traffic, per station
#     Format all Subway station names - Entity recognition problem - Mapping between datasets
#     Deduplicate the subway stations, in the case where there are different entrances and entrance types
#     
# These steps are not in the following report are they don't include visualization but are available on the girhub repository.
# 
# Below is a snapshot of the different datasets in their preprocessed format, before merging.

# In[2]:

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# In[3]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.preprocessing import StandardScaler
import math
import operator
from geopy.distance import vincenty
import distance
import json
import colorlover as cl
get_ipython().magic(u'matplotlib inline')

import warnings
warnings.filterwarnings('ignore')


# ### Income - Neighborhood

# In[4]:

nei = pd.read_csv('data/neighborhoods.csv', sep=';')
nei['X'] = nei['X'].apply(lambda x: "-{:.6f}".format(x))
nei['Y'] = nei['Y'].apply(lambda x: "{:.6f}".format(x))

meancome = np.mean(nei['Median Income'])
nei.index = nei['Neighborhood']
nei.head()


# ### Art Galleries

# In[5]:

gal = pd.read_csv('data/galleries_untouched.csv', sep=',')


# In[6]:

gal['Y'] = gal['the_geom'].apply(lambda x: x.split(' ')[2].strip(')')[:9])
gal['X'] = gal['the_geom'].apply(lambda x: x.split(' ')[1].strip('(')[:10])
del gal['the_geom']
del gal['ADDRESS2']
gal = gal[['NAME','Y','X','TEL','URL','ADDRESS1','CITY','ZIP']]


# In[7]:

gal.head()


# ### Subway Stations

# In[8]:

sta = pd.read_csv('data/stations_coord_entrance.csv', sep=';')


# In[9]:

types={'Stair':0,'Door':1,'Walkway':2,'Ramp': 3, 'Easement':4, 'Escalator':5, 'Elevator': 6}
sta['Entrance'] = sta['Entrance'].map(types)
types_rev={'0':'Stair','1':'Door','2':'Walkway','3':'Ramp','4':'Easement','5':'Escalator','6':'Elevator'}
types_col={'Stair':'r','Door':'g','Walkway':'b','Ramp': 'y', 'Easement':'b', 'Escalator':'r', 'Elevator': 'g'}

ent = {nam:[] for nam in sta['Name']}
for k in range(len(sta)):
    ent[sta['Name'][k]].append(sta['Entrance'][k])
ent = {sta: types_rev[str(max(ent[sta]))] for sta in ent.keys()}

del sta['Entrance']
sta = sta.groupby('Name').mean()
sta['Name'] = sta.index
sta.index = range(len(sta))

sta['Entrance'] = sta['Name'].apply(lambda x: ent[x])
sta['X'] = sta['X'].apply(lambda x: "{:.6f}".format(x))
sta['Y'] = sta['Y'].apply(lambda x: "{:.6f}".format(x))

sta = sta[['Name','Y','X','Entrance']]
sta.head()


# ### Subway Traffic

# For each station, we have the traffic (sum of entries and exits per day) for 6 consecutive days: 
# 
#     April 8th 2017
#     April 9th 2017
#     April 10th 2017
#     April 11th 2017
#     April 12th 2017
#     April 13th 2017

# In[10]:

sta_traffic = pd.read_csv('data/station_traffic.csv')


# In[11]:

#Map those station names to the ones in the DataFrame sta, that has all information on stations
sta_traffic['Name'] = sta_traffic['Name'].apply(lambda x:str.lower(x))


# In[12]:

with open('data/map_station_names.json','r') as f:
    map_names = json.load(f)
map_names_rev = {str(bad):str(good) for good,bad in map_names.iteritems()}


# In[13]:

map_names_normal = {orig_name: orig_name.lower() for orig_name in sta['Name']}
map_names_normal_rev = {low:orig for orig, low in map_names_normal.iteritems()}

map_final = {bad: map_names_normal_rev[good] for bad, good in map_names_rev.iteritems()}
sta_traffic['Name'] = sta_traffic['Name'].map(map_final)


# In[14]:

sta_traffic = sta_traffic.dropna()
sta_traffic['traffic_mean'] = (sta_traffic['traffic_april8']+sta_traffic['traffic_april9']+sta_traffic['traffic_april10']+sta_traffic['traffic_april11']+sta_traffic['traffic_april12']+sta_traffic['traffic_april13'])/6


# In[15]:

sta_traffic.head()


# ## Merging the diverse datasets
# 
# The final dataset is a dataset where for each subway station, we have all required information:
#     Name
#     Number of art galleries
#     Median Income
#     Traffic
#     Entrance Type
#     
# Basically, we started with the dataset where each subway station is described. Then:
#     
#     Compute the number of art galleries within 0.2 miles of the station, using GPS Coordinates of the galleries
#     
#     Assign a neighborhood and a median income, using GPS Coordinates of the neighborhood centroids
#     
#     Join the obtained dataset with the dataset containing the traffic data, using a mapping between two different formats for the names of the stations, that we computed using Stemming and Levenstein Distance 

# Note that some stations don't have a neighborhood as we focused on neighborhoods near Manhattan. We only keep those stations afterwards. We also filter out the stations that have less than 2 galleries around, in order to make to visualizations more readable and because those stations are not very interesting based on our assumptions.

# In[16]:

#This function computes the distance, in miles, between two GPS points.
def dist(x1, x2, y1, y2):
    dist = vincenty((x1, y1), (x2, y2)).miles
    return dist


# In[17]:

sta_nbgal={sta_name: 0 for sta_name in sta['Name']}
sta_neighborhood={sta_name: '' for sta_name in sta['Name']}


# In[18]:

for k in range(len(sta)):
    x1 = sta['X'][k]
    y1 = sta['Y'][k]
    station = sta['Name'][k]
    for j in range(len(gal)):
        dz = dist(x1, gal['X'][j], y1, gal['Y'][j])
        if dz < 0.2:
            sta_nbgal[station] += 1
    min_dz = 999
    for l in range(len(nei)):
        dz = dist(x1, nei['X'][l], y1, nei['Y'][l])
        if dz < min_dz and dz < 4:
            min_dz = dz
            sta_neighborhood[station]=nei['Neighborhood'][l]


# In[19]:

sta['Nb_gal'] = sta['Name'].map(sta_nbgal)
sta['Neighborhood'] = sta['Name'].map(sta_neighborhood)


# Snapshot of the dataset of the Subway stations, before merging the traffic data, but after computation of the number of galleries and join with the neighborhood dataset

# In[20]:

sta = sta.join(nei, on='Neighborhood', how='left', lsuffix='', rsuffix='_nei')
sta = sta[['Name','Y','X','Entrance','Nb_gal','Neighborhood','Median Income']]
sta.head()


# In[21]:

sta_traffic.index = sta_traffic['Name']


# In[22]:

sta = sta.join(sta_traffic, on='Name', how='left', lsuffix='', rsuffix='_nei')


# In[23]:

sta = sta.dropna()
del sta['Name_nei']


# In[24]:

sta.index = sta['Name']
sta = sta[sta['Nb_gal']>2]


# ### Final datasets, ready for the visualization tasks
# 
# Here is a snapshot of the final dataset

# In[25]:

sta.head()


# # Exploratory Data Analysis
# ## Interactive plots using plotly, please play with it!

# In[26]:

import plotly.plotly as py
import cufflinks as cf
import plotly.graph_objs as go
from plotly.graph_objs import *


# In[27]:

import plotly
plotly.offline.init_notebook_mode()
cf.set_config_file(offline=False, world_readable=True, theme='ggplot')


# ## First set of simple plots, in order to understand the different variables
# 
#     Type of Entrance
#     Density in Art Galleries
#     Median Income of the neighborhood
#     Traffic

# ### Type of Entrance

# In[28]:

data = [go.Bar(
            x=sta['Entrance'].value_counts().index,
            y=list(sta['Entrance'].value_counts()),
            marker=dict(color='rgb(62,57,193)')
    )]
layout = go.Layout(
    title="Type of Entrance - Frequency"
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# Most stations have Stairs, which can be a problem if the artworks are very heavy or large for instance. An artist may want to select a station that has an elevator.

# ### Density in Art Galleries

# In[55]:

data = [go.Bar(
            y=sta['Nb_gal'].sort_values(ascending=False)[:30].index[::-1],
            x=sta['Nb_gal'].sort_values(ascending=False)[:30][::-1],
            marker=dict(color='rgb(62,57,193)'),
            text= ['galleries around<br><b>'+sta['Neighborhood'][sta['Nb_gal'].sort_values(ascending=False)[:30].index[::-1][k]]+'</b>' for k in range(30)],
            orientation = 'h'
    )]
layout = go.Layout(
    autosize=False,
    width=1000,
    height=700,
    margin=go.Margin(
        l=170,
        r=30,
        b=100,
        t=100,
        pad=4
    ),
    title="Number of galleries around each Subway Station",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        autotick=False,
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Number of art galeries within 0.2 miles'
    ),
    bargap=0.4
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# We find reassuring insights: 68th St-Hunter College, Lexington Av for instance are in the Upper East Side, in the Museum area - MET, Guggenheim... - where the art gallery density is indeed very high.
# 
# Spring St, Canal St, Prince St are in very arty areas downtown Manhattan, it is thus a good thing to find them at the top of our ranking.

# ### Mean Traffic per station

# In[57]:

data = [go.Bar(
            y=sta['traffic_mean'].sort_values(ascending=False)[:30].index[::-1],
            x=sta['traffic_mean'].sort_values(ascending=False)[:30][::-1],
            marker=dict(color='rgb(62,57,193)'),
            text= ['<b>'+sta['Neighborhood'][sta['traffic_mean'].sort_values(ascending=False)[:30].index[::-1][k]]+'</b>' for k in range(30)],
            orientation = 'h'
    )]
layout = go.Layout(
    autosize=False,
    width=900,
    height=700,
    margin=go.Margin(
        l=210,
        r=0,
        b=100,
        t=100,
        pad=4
    ),
    title="Mean daily traffic for each Subway Station",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        autotick=False,
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Mean daily traffic'
    ),
    bargap=0.4
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# There is not much surprise on the Traffic either. Grand Central, 34th St and 42nd St are known to be the main train stations in Manhattan, with a massive daily traffic. We still see that the slope is pretty high at the top of the ranking, meaning that there are a few stations with a massive traffic and a lot of stations with a more homogeneous traffic, around 50k people per day.

# ### Median Income per station

# In[56]:

data = [go.Bar(
            y=sta['Median Income'].sort_values(ascending=False)[:30].index[::-1],
            x=sta['Median Income'].sort_values(ascending=False)[:30][::-1],
            marker=dict(color='rgb(62,57,193)'),
            text= ['<b>'+sta['Neighborhood'][sta['Median Income'].sort_values(ascending=False)[:30].index[::-1][k]]+'</b>' for k in range(30)],
            orientation = 'h'
    )]
layout = go.Layout(
    autosize=False,
    width=900,
    height=700,
    margin=go.Margin(
        l=210,
        r=0,
        b=100,
        t=100,
        pad=4
    ),
    title="Median Income around each Subway Station (k$)",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        autotick=False,
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Median Income'
    ),
    bargap=0.4
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# The bars here are grouped by neighborhood basically. This is due to the way we computed the median income for each station, as we assigned to each station the income of its neighborhood. 
# 
# We find the stations in the richest neighborhood on top (Chambers St in Tribeca, Whitehall St in Battery Park, Lexington Av in N. Sutton Area...)

# ## Combination of the variables

# In the following charts, we combine the different variables, in order to gain insights on the subway stations to pick.
# 
# ### Number of art galleries vs Traffic
# 
# In this first scatter plot,
# 
#     dot: a subway station
#     y coordinate: number of art galleries around
#     x coordinate: mean traffic

# In[51]:

data = [go.Scatter(
        x = sta['traffic_mean'], 
        y = sta['Nb_gal'], 
        text = sta['Name'], 
        mode = 'markers', 
        name = 'Subway station',
        marker = dict(
            size = 13,
            color = 'rgb(62,57,193)'
        )
    )]
layout = go.Layout(
    hovermode="closest", 
    autosize=False,
    width=1000,
    height=700,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    title="Scatter plot of the Subway Stations",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        title='Density of art Galleries'
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Mean Traffic'
    ),
    bargap=0.4
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# IPython notebook
# py.iplot(fig, filename='pandas/multiple-scatter')


# Based on this plot, we can combine our observations on the traffic and the density of art galleries. Typically the subway stations are polarized along the axis. There are no stations with a massive traffic as well as a large number of galleries. There is mostly a trade off between an arty station and a station with a lot of traffic, except for a few stations such as Canal St or West 4. We will go deeper in the analysis in the charts below.
# 
# However, we have absolute values for both features, which is not optimal for our task of selecting the subway station that would match with an artist, based on their criteria.
# 
# By scaling the variables Number of art galleries and Traffic (retrieveing the mean and dividing by the standard deviation), we will be able to see what stations are more arty than the majority, and which ones have more traffic than the mean!

# ### Number of art galleries vs Traffic - Scaled
# 
# In the following plot, we have scaled the data.
# As a consequence of that, the dot in the upper right part of the graph have more traffic and more galleries than the majority of stations, those in the upper left part have more galleries but less traffic, those in the lower left part have less galleries and less traffic and those in the lower right part have more traffic but less galleries.
# 
# These four groups have been assigned different colors

# In[34]:

sta['traffic_scaled'] = sta['traffic_mean']
sta['traffic_scaled'] = sta['traffic_scaled'].apply(lambda x: (x-np.mean(sta['traffic_mean']))/np.std(sta['traffic_mean']))

sta['nbgal_scaled'] = sta['Nb_gal']
sta['nbgal_scaled'] = sta['nbgal_scaled'].apply(lambda x: (x-np.mean(sta['Nb_gal']))/np.std(sta['Nb_gal']))


# In[35]:

sta['quad'] = 0
for k in range(len(sta['quad'])):
    if sta['traffic_scaled'][k]<0:
        if sta['nbgal_scaled'][k]<0:
            sta['quad'][k]=1
        else:
            sta['quad'][k]=2
    else:
        if sta['nbgal_scaled'][k]<0:
            sta['quad'][k]=3
        else:
            sta['quad'][k]=4


# In[44]:

data = [go.Scatter(
        x = sta[sta['quad']==1]['traffic_scaled'],y = sta[sta['quad']==1]['nbgal_scaled'],
        text = sta[sta['quad']==1]['Name'],mode = 'markers', 
        name = 'Low art / Low traffic',marker = dict(size = 13,color = 'rgb(255,215,0)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==2]['traffic_scaled'],y = sta[sta['quad']==2]['nbgal_scaled'],
        text = sta[sta['quad']==2]['Name'],mode = 'markers', 
        name = 'High art / Low traffic',marker = dict(size = 13,color = 'rgb(34,139,34)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==3]['traffic_scaled'],y = sta[sta['quad']==3]['nbgal_scaled'],
        text = sta[sta['quad']==3]['Name'],mode = 'markers', 
        name = 'Low art / High traffic',marker = dict(size = 13,color = 'rgb(240,128,128)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==4]['traffic_scaled'],y = sta[sta['quad']==4]['nbgal_scaled'],
        text = sta[sta['quad']==4]['Name'],mode = 'markers', 
        name = 'High art / High traffic',marker = dict(size = 13,color = 'rgb(100,149,237)',opacity=0.9)),
       ]
layout = go.Layout(
    hovermode="closest", 
    autosize=False,
    width=1000,
    height=700,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    title="Scatter plot of the Subway Stations",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        title='Density of art Galleries'
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Mean Traffic'
    ),
    showlegend=True
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# As described above and in the legend of the plot, we have defined four groups of art galleries.
# 
# 
# Below is an example of how to read this plot:
# 
# An artist who doesn't want to engage with arty people but wants to reach the larger audience as possible would probably pick a station in the red group, such as 42nd St.
# 
# An artist who wants a lot of traffic as well as engaging with arty people would try a station in the blue group, such as West 4 or Canal St.
# 
# An artist who wants to be in a rather calm station - low traffic - but with arty people may want to go to Spring St or Lexington Av!
# 
# And an artist who wants neither traffic nor arty commuters may pick a station in the yellow group!
# 
# Yet, this plot doesn't talk about the mean income of people living near the station, and thus likely to commute through the station. We will add this feature in the next plot.

# ### Number of art galleries vs Traffic vs Income - Scaled

# In this plot, the size of the dot is correlated to the median income of the neighborhood the station is located in.

# In[37]:

def bin_income(x):
    if x<50:
        return 11
    elif 50<x<100:
        return 15
    elif 100<x<150:
        return 20
    else:
        return 27


# In[38]:

sta['income_binned'] = sta['Median Income'] 
sta['income_binned'] = sta['income_binned'].apply(lambda x: bin_income(x))


# In[43]:

data = [go.Scatter(
        x = sta[sta['quad']==1]['traffic_scaled'],y = sta[sta['quad']==1]['nbgal_scaled'],
        text = sta[sta['quad']==1]['Name'],mode = 'markers',name = 'Low art / Low traffic',
        marker = dict(size = sta[sta['quad']==1]['income_binned'],color = 'rgb(255,215,0)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==2]['traffic_scaled'],y = sta[sta['quad']==2]['nbgal_scaled'],
        text = sta[sta['quad']==2]['Name'],mode = 'markers',name = 'High art / Low traffic',
        marker = dict(size = sta[sta['quad']==2]['income_binned'],color = 'rgb(34,139,34)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==3]['traffic_scaled'],y = sta[sta['quad']==3]['nbgal_scaled'],
        text = sta[sta['quad']==3]['Name'],mode = 'markers',name = 'Low art / High traffic',
        marker = dict(size = sta[sta['quad']==3]['income_binned'],color = 'rgb(240,128,128)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['quad']==4]['traffic_scaled'],y = sta[sta['quad']==4]['nbgal_scaled'],
        text = sta[sta['quad']==4]['Name'],mode = 'markers',name = 'High art / High traffic',
        marker = dict(size = sta[sta['quad']==4]['income_binned'],color = 'rgb(100,149,237)',opacity=0.9)),
       ]
layout = go.Layout(
    hovermode="closest", 
    autosize=False,
    width=1000,
    height=700,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    title="Scatter plot of the Subway Stations",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        title='Density of art Galleries'
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Mean Traffic'
    ),
    showlegend=True
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# We can now complete our analysis!
# 
# Let's say the artist really wants to sell his artworks and not only display it.
# 
# If he finds himself in the blue group, he may prefer West 4th over Canal St.
# 
# If he chose the red group, he may stay away from Bedford Ave and go to 59th Columbus Circle or 42nd st.
# 
# If the green group took his preference, Lexington Av would be a better option than Prince St for instance!
# 

# ### Number of art galleries vs Traffic vs Entrance type - Scaled

# We replace the feature 'Income' by the feature 'Entrance' to maintain a great readability of the graph. As there are 5 types of Entrance, we assign a color to each type of Entrance, as descirbed in the legend.

# In[42]:

data = [go.Scatter(
        x = sta[sta['Entrance']=='Stair']['traffic_scaled'],y = sta[sta['Entrance']=='Stair']['nbgal_scaled'],
        text = sta[sta['Entrance']=='Stair']['Name'],mode = 'markers',name = 'Stair',
        marker = dict(size = 15,color = 'rgb(255,192,203)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['Entrance']=='Door']['traffic_scaled'],y = sta[sta['Entrance']=='Door']['nbgal_scaled'],
        text = sta[sta['Entrance']=='Door']['Name'],mode = 'markers',name = 'Door',
        marker = dict(size = 15,color = 'rgb(0,0,205)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['Entrance']=='Easement']['traffic_scaled'],y = sta[sta['Entrance']=='Easement']['nbgal_scaled'],
        text = sta[sta['Entrance']=='Easement']['Name'],mode = 'markers',name = 'Easement',
        marker = dict(size = 15,color = 'rgb(138,43,226)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['Entrance']=='Escalator']['traffic_scaled'],y = sta[sta['Entrance']=='Escalator']['nbgal_scaled'],
        text = sta[sta['Entrance']=='Escalator']['Name'],mode = 'markers',name = 'Escalator',
        marker = dict(size = 15,color = 'rgb(139,0,139)',opacity=0.9)),
        go.Scatter(
        x = sta[sta['Entrance']=='Elevator']['traffic_scaled'],y = sta[sta['Entrance']=='Elevator']['nbgal_scaled'],
        text = sta[sta['Entrance']=='Elevator']['Name'],mode = 'markers',name = 'Elevator',
        marker = dict(size = 15,color = 'rgb(255,20,147)',opacity=0.9))
       ]
layout = go.Layout(
    hovermode="closest", 
    autosize=False,
    width=1000,
    height=700,
    margin=go.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    title="Scatter plot of the Subway Stations - Entrance Type",
    yaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showticklabels=True,
        ticks='outside',
        title='Density of art Galleries'
    ),
    xaxis=dict(
        titlefont=dict(
            family='Arial, sans-serif',
            size=18,
            color='lightgrey'
        ),
        showgrid=True,
        showticklabels=True,
        ticks='outside',
        title='Mean Traffic'
    ),
    showlegend=True
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.iplot(fig)


# #### If the artist says "I only want to showcase my art, not sell it! But it is very heavy and I have broken my ankle, I may need an elevator!"
# 
# This artist should look for the Light Pink dots, in the upper left corner, as he doesn't particularly want to sell.
# 
# We would recommend him to try Lexington Av or 34 St Hudson Yards! 

# ## What next? 
# 
# In the nearest future, build a recommandation algorithm, that would recommand a subway station to an artist, based on its preferences. We would then add this recommandation system to this web app :)
