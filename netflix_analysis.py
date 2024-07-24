import pandas as pd # for prepping data
import numpy as np # for mathematical calc or linear calc
# import matplotlib # data visuals
import plotly.express as px # data visuals
from textblob import TextBlob # for sentiment analysis

# read the data into dataframe using pandas
df=pd.read_csv(r"C:\Users\sania\Downloads\archive (2)\netflix_titles.csv")
print(df.shape) #printts total data (rows,cols); in jupyter df.shape()
print(df.columns) # prints names of all the columns

# analyze the ratings of content
z = df.groupby(['rating']).size().reset_index(name='counts')
print(z)
pieChart = px.pie(z, values='counts', names='rating', title='Distribution of Content Ratings on Netflix', 
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()

# Filling null values for directors column
df['director']=df['director'].fillna('No Director Specified')


filtered_directors=pd.DataFrame()  # create an empty dataframe
filtered_directors=df['director'].str.split(',',expand=True).stack()  #get the names of all the directors separated by commas 
filtered_directors=filtered_directors.to_frame() # to_frames get the values into a column format
filtered_directors.columns=['Director'] # we are renaming the col as Director
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content') # grouping the directors on the basis of films
directors=directors[directors.Director !='No Director Specified']  #removing the null values
directors=directors.sort_values(by=['Total Content'],ascending=False) # sorting on the basis of the number of movies
directorsTop5=directors.head() # top values
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
print(directorsTop5)
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()


# Filling null values for cast column
df['cast']=df['cast'].fillna('No cast Specified')


filtered_cast=pd.DataFrame()  # create an empty dataframe
filtered_cast=df['cast'].str.split(',',expand=True).stack()  #get the names of all the cast separated by commas 
filtered_cast=filtered_cast.to_frame() # to_frames get the values into a column format
filtered_cast.columns=['Cast'] # we are renaming the col as Cast
cast=filtered_cast.groupby(['Cast']).size().reset_index(name='Total Content') # grouping the cast on the basis of films
cast=cast[cast.Cast !='No cast Specified']  #removing the null values
cast=cast.sort_values(by=['Total Content'],ascending=False) # sorting on the basis of the number of movies
castTop5=cast.head() # top values
castTop5=castTop5.sort_values(by=['Total Content'])
print(castTop5)
fig2=px.bar(castTop5,x='Total Content',y='Cast',title='Top 5 Actors on Netflix')
fig2.show()



#trends of production i.e., movies and shows line graph

df1=df[['type','release_year']] #taking two cols year and their type
df1=df1.rename(columns={"release_year": "Release Year"}) # renaming release_year
df2=df1.groupby(['Release Year','type']).size().reset_index(name='Total Content') #grouping them on the basis of year first then type
df2=df2[df2['Release Year']>=2010]
fig3 = px.line(df2, x="Release Year", y="Total Content", color='type',title='Trend of content produced over the years on Netflix')
fig3.show()

#sentiment analysis

dfx=df[['release_year','description']]
dfx=dfx.rename(columns={'release_year':'Release Year'})
for index,row in dfx.iterrows():
    z=row['description']
    testimonial=TextBlob(z)
    p=testimonial.sentiment.polarity
    if p==0:
        sent='Neutral'
    elif p>0:
        sent='Positive'
    else:
        sent='Negative'
    dfx.loc[[index,2],'Sentiment']=sent


dfx=dfx.groupby(['Release Year','Sentiment']).size().reset_index(name='Total Content') # grouping the release year based on sentiment

dfx=dfx[dfx['Release Year']>=2010]
fig4 = px.bar(dfx, x="Release Year", y="Total Content", color="Sentiment", title="Sentiment of content on Netflix")
fig4.show()