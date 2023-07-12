
import numpy as np
import pandas as pd


df_can = pd.read_excel('Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

print('Below shows the original data:\n', df_can.head(5))

#Drop some columns
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print('Below shows the data after some columns have been dropped:\n', df_can.head(2))

#rename columns
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

#add column 'Total'
df_can['Total'] = df_can.sum(axis=1)

#check how many null objects we have
print(df_can.isnull().sum())

#summary of dataset
print(df_can.describe())

#set country as the index
df_can.set_index('Country', inplace=True)
print('Below shows the data with Country set to the index:\n', df_can.head(2))

#convert column names to string to limit ambiguity
df_can.columns = list(map(str, df_can.columns))
[print (type(x)) for x in df_can.columns.values]

years = list(map(str, range(1980, 2014)))
print(years)


#filtering based on criteria
#create a condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)
print('Below shows the Asian countries immigration to Canada:\n', df_can[condition])

#filter for area name = asia and regname = southern asia
print('Below shows the Southern Asian Countries immigration to Canada:\n',
      df_can[(df_can['Continent'] == 'Asia') & (df_can['Region']=='Southern Asia')])

#changes made
print('data dimensions:', df_can.shape,
      '\n', df_can.columns,
'\n', df_can.head(2))


#visualising data
import matplotlib as mpl
import matplotlib.pyplot as plt
print('Matplotlib version:', mpl.__version__)

#apply a style
print(plt.style.available)
mpl.style.use(['ggplot'])


#Plot a line graoh of immigration from hati using df.plot()
haiti = df_can.loc['Haiti', years]
print('Below shows the immigration data for Haiti:\n', haiti.head(2))


#change data to interger for plotting
haiti.index = haiti.index.map(int)
haiti.plot(kind='line')
plt.title('Immigration from Haiti to Canada')
plt.xlabel('Years')
plt.ylabel('Number of immigrants')
plt.text(2000, 6000, '2010 Earthquake')
plt.show()
plt.close()


#compare the number of immigrants for China and India

df_CI_to_Can = df_can.loc[['China', 'India'], years]
print('Below shows the data for China and India immigration to Canada:\n', df_CI_to_Can)

#plot the graph
df_CI_to_Can.plot(kind='line')
plt.show()

#the graph looks strange need to transpose
df_CI_to_Can = df_CI_to_Can.transpose()
df_CI_to_Can.plot(kind='line')
plt.title('Immigration to Canada from China and India')
plt.xlabel('Years')
plt.ylabel('Number of immigrants')
plt.show()


#compare the trend of the top 5 countries with immigration to canada
df_can.sort_values(by='Total', axis=0, ascending=False, inplace=True)
df_top5 = df_can.head(5)

print(df_top5)

df_top5 = df_top5[years].transpose()
df_top5.index = df_top5.index.map(int)
df_top5.plot(kind='line', figsize=(14, 8))
plt.title('Top 5 countries immigrating to Canada')
plt.xlabel('Years')
plt.ylabel('Number of immigrants')
plt.show()