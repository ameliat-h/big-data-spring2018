import pandas as pd
import numpy as np

#create empty Dataframe
df = pd.DataFrame()

#create a columnd
df['name'] = ['Joey', 'Jeremy', 'Jenny']

#view Dataframe
df

#assign a new colum nto df called "age" with a list of ages
df.assign(age = [28, 33, 27])

df = pd.read_csv('data/skyhook_2017-07.csv', sep=',')

# now print the first 5 rows of the Dataframe
df.head()

#this shows us the data types of each column
df.dtypes

#this determines the shape (i.e. the dimensions) of our dataframe by accessing its shape property
df.shape

#number of rows?
df.shape[0]
#number of columns
df.shape[1]

#retrieve data frame column names, accesses columns property. also looks at the data type of the object returned by df.columns
df.columns
type(df.columns)

#access an individual column
df.cat_name

#accesses count column: [ this refers to a specific Pandas function that counts the number of non-null observations over a given axis (which we didn't specify).]
df.count

#this one is a more explicit syntax than above
df['count']

# use unique() method to find the unique values in each column
df.lat.unique()

# multiple columns:
df_multipleColumns = df[['hour', 'cat', 'count']]
df_multipleColumns.head()

###ON TO QUERYING!!!
#WITH PANDAS, you can take a small subset of the dataframe, run a filter or query on it, and then use that query to apply to other parts of the df

#output of this is a series containing the truth of falsehood of our query (###???) - THIS IS CALLED A mask

df['hour'] == 158

#now we want to apply a filter, using the mask to "index" into the dataframe to get the rows we want:
time = df[df['hour'] == 158]
time.head
time.shape

# queries can be based on multiple criteria using boolean operators — just add () around each condition. each condition creates a mask containing true and false values

df[(df['hour'] == 158) & (df['count'] < 50)]

# this dataset has now been substantially filtered, limited to single hour and limited to those cells with more than 50 GSP pings.

#how to specify a certain day?
bastille = df[df['date'] == '2017-07-14']
bastille.head

#which aggregated cells saw greater than average levels of activity?
bastille_enthusiasts = bastille[bastille['count'] > bastille['count'].mean()]
bastille_enthusiasts.head

# the .describe() method can be used to return a table that includes the count of non-null rows, their mean, standard dev, etc.
bastille_enthusiasts['count'].describe()

#what if we wanted to find summary stats for each day in July? use .groupby() method to collapse a dataframe on the values stored in a given column. out put is a table in which each row represents a table, and each column is a summary stat of the 'count' column
df.groupby('date')['count'].describe()

# group by multiple columns too! let's calculate summ stats for 'count' column for each hour of each day:

#you can also use built-in pandas methods to calculate individual summary stats
df['count'].max()
df['count'].min()
df['count'].mean()
df['count'].std()
df['count'].count()

#you can save these as variables! then cast them to strings!!
max_count = df['count'].max()
min_count = df['count'].min()
mean_count = df['count'].mean()

#now print those results:
print(f"Maximum number of GPS pings: {max_count}")
print(f"Minimum number of GPS pings: {min_count}")
print(f"Average number of GPS pings: {mean_count}")

#what if you're interested in returning all the other columns associated with those minimum and maximum values?

#there's a single row that contains the maximum alue of GPS pings.
df[df['count'] == df['count'].min()]

#moving onto the cleaning stage...
#this line lets us plot in Atom
import matplotlib
#this line allows the result of plots to be displayed inline with our code.
%matplotlib inline
