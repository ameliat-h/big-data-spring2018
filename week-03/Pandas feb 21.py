import pandas as pd
import numpy as np

import matplotlib
%matplotlib inline



new_list = []
df = pd.Dataframe()
print(df)

#identifying a column and creating entries in a table for that given column
df['name'] = ['Bilbo', 'Frodo', 'Samwise']

df

df.assign(height = [0.5, 0.4, 0.6])
#changes working directory to the week-03 subfolder
import os
os.chdir('week-03')

df = pd.read_csv('data/skyhook_2018-07.csv', sep=',')

df.head()

df.shape() #returns paired collection of values (x, y) where x is columns and rows is y
df.columns #gives us index that includes all of our column names
df['cat_name'].unique() #finds names of possible categories for those
df['cat_name']
df.cat_name

#data frame, please take this mask and return only those rows where this mask contains the boolean value of true
one_fifty_eight = df[df['hour']] == 158

df[df['hour']] == 158 & (df['count'] > 50)].shape

#creating subset of data frame where dates are equal to this one
bastille = df[df['date'] == '2017-07-14']
bastille.head()
# asking for rows where the count column is > than the count column's mean
lovers_of_bastille = bastille[bastille['count'] > bastille['count'].mean()]

#looks for unique date values and sum all of the values found in teh count column for each unique data
df.groupby('date')['count'].sum()

df['count'].max() #returns max
df['count'].min()
df['count'].mean() #avg
df['count'].std() #standard deviation
df['count'].count()



#how do we make data frames more usuable?
#ie the way time is stored in this df is weird, by hours in a week
df['hour'].unique()
jul_sec = df[df['date'] == '2017-17-02']

jul_sec.groupby('hour)['count'].sum().plot()

df['date_new'] = pd.t_datetime(df['date'], format='%Y-%m-%d')

df['weekday'] = df['date_new'].apply(lambda x: x.weekday() + 1)

#define new column for weekday
df['date_new'] == '2017-07-02']['weekday'] + 1)

for i in range(0, 168, 24):
    df.drop(df[df['weekday'] == (i/24) &
    (
    (df['hour']) < j | df['hour'] > j + 18)
    )
    ])
