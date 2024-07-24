import pandas as pd # data manipulation
import numpy as np # linear math and calc   
import matplotlib.pyplot as plt  # static and interactive graphs
import seaborn as sns #statistical graphs
import plotly.express as px  # entire figure at once



data = pd.read_csv(r"C:\Users\sania\Downloads\archive (4)\Instagram_data.csv", encoding = 'latin1')
print(data.head())

data.isnull().sum()
d=data.info()
print(d)

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight') # a style in matplotlib that gives a sleek modern look, inspired by the website Five ThirtyEight
plt.title("Distribution of Impressions From Home") # title of the plot
sns.histplot(data['From Home']) # combines a histogram and a kernel density estimate (KDE) plot from seaborn
plt.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Hashtags")
sns.histplot(data['From Hashtags'])
plt.show()

plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Distribution of Impressions From Explore")
sns.histplot(data['From Explore'])
plt.show()


home = data["From Home"].sum()
hashtags = data["From Hashtags"].sum()
explore = data["From Explore"].sum()
other = data["From Other"].sum()

labels = ['From Home','From Hashtags','From Explore','Other']
values = [home, hashtags, explore, other]

fig = px.pie(data, values=values, names=labels, 
             title='Impressions on Instagram Posts From Various Sources', hole=0.5)
fig.show()