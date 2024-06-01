# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 03:19:08 2024

@author: SÜLEYMAN BEYYY
"""

#Importing Pandas:
'''
import pandas as pd 
'''
#Create a series:
'''
import pandas as pd
series = pd.Series([10,20,30,40,50])
print(series) 
'''
#Serial indexing and slicing:
'''
import pandas as pd 
series = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(series['c'])
print(series[['a','b','e']])
print(series[2:4])
'''
#Accessing the Series and Assigning Values:
'''
import pandas as pd 
series = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])   
print(series['b'])
series['b'] = 25
print(series)
'''
#Data Frames:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df)
'''
#Data frame indexing and slicing:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.loc[0])
print(df['Student'])
print(df[df['Point']>85])
'''
#Adding Columns:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
df['Year'] = [15,16,15,17]
print(df)
'''
#Delete Column:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df)
df.drop('Point',axis=1,inplace=True)
print(df)
'''
#Rename Column:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df)
df.rename(columns={'Class':'Level'},inplace=True)
print(df)
'''
#head() function:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.head(2))
'''
#info() function:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.info())
'''
#describe() function:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.describe())
'''
#shape feature:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.shape)   
'''
#Showing Column Names:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.columns)      
'''
#Showing data types:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)
print(df.dtypes)    
'''
#Reading Data from CSV File:
'''
import pandas as pd 
df = pd.read_csv('ornek.csv')
print(df)
'''
#Reading Data from Excel File:
'''
import pandas as pd 
df = pd.read_excel('veri.xlsx',sheet_name='Sheet1')    
print(df)
'''
#Writing Data Frame to CSV Format:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)    
df.to_csv('data.csv',index=False)
'''
#Writing Data Frame to Excel Format:
'''
import pandas as pd
data = {'Student': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma'],
'Class': [10, 11, 10, 12],
'Point': [85, 92, 78, 88]}
df = pd.DataFrame(data)    
df.to_excel('data.xlsx',sheet_name='Sheet1',index=False)
'''
#Deleting Missing Data:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,6,7,None,9]})
df.dropna(inplace=True)
print(df)
'''
#Filling Missing Data:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,6,7,None,9]})
df.fillna(0,inplace=True)
print(df)    
'''
#Filling Missing Data with Average Value:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,6,7,None,9]})
df['A'].fillna(df['A'].mean(),inplace=True)
df['B'].fillna(df['B'].mean(),inplace=True)
print(df)
'''
#Filling Missing Data Forward:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,6,7,None,9]})
print(df.ffill())
'''
#Filling in Missing Data Backwards:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,None,4,5],'B':[None,6,7,None,9]})
print(df.bfill())
'''
#Converting Data Types:
'''
import pandas as pd 
df = pd.DataFrame({'A':[1,2,3],'B':[4.5,5.6,6.7],'C':['7','8','9']})
print(df)
df['A'] = df['A'].astype(float)
df['B'] = df['B'].astype(int)
df['C'] = df['C'].astype(str)
print(df)
'''
#Date and Time Conversions:
'''
import pandas as pd 
df = pd.DataFrame({'Date':['2021-01-01','2022-02-02','2023-03-03'],'Time':['12:00:00','13:30:00','15:45:00']})
df['Date'] = pd.to_datetime(df['Date'])
df['Time'] = pd.to_datetime(df['Time'],format='%H:%M:%S').dt.time
print(df)    
'''
#Transforming Columns:
'''
import pandas as pd 
df = pd.DataFrame({'Category':['A','B','C'],'Values':[10,20,30]})    
df['New_Category'] = df['Category'].apply(lambda x: x.lower())
print(df)
'''
#Reshaping Columns:
'''
import pandas as pd
df = pd.DataFrame({'Student':['Ali','Ayşe','Mehmet'],'Lesson':['Mathematics', 'Physics', 'Chemistry'],'Point':[90,85,95]})
df_pivot = df.pivot(index='Student',columns='Lesson',values='Point')
print(df_pivot)
'''
#Merge Columns:
'''
import pandas as pd 
df1 = pd.DataFrame({'Student':['Ali','Ayşe','Mehmet'],'Lesson1':[90,85,95]})
df2 = pd.DataFrame({'Student':['Ali','Ayşe','Mehmet'],'Lesson2':[80,75,85]})
df_merge = pd.merge(df1,df2,on='Student')
print(df_merge)
'''
#Remove duplicate or unnecessary data from a dataframe:
'''
import pandas as pd 
df = pd.DataFrame({'Category':['A','B','C','A','B'],'Values':[10,20,30,10,40]})
df_unique = df.drop_duplicates()
print(df_unique)
'''
#Data Analysis and Statistical Calculations:
'''
import pandas as pd 
df = pd.DataFrame({
'Student': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru',
'Can', 'Deniz', 'Gizem',
'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül',
'Kadir', 'İrem', 'Ozan'],
'Lesson': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik'],
'Point': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83,
94, 81, 84, 90]
})   
print(df.head(5))
print('Average: ',df['Point'].mean())
print('Median: ',df['Point'].median())
print('Mode: ',df['Point'].mode())
print('Total: ',df['Point'].sum())
print('Minimum: ',df['Point'].min())
print('Maximum: ',df['Point'].max())
print('Standard deviation: ',df['Point'].std())
print('Variance: ',df['Point'].var())
print('Number of values: ',df['Point'].count())
print('Percentiles (25%, 50%, 75%): ',df['Point'].quantile([0.25,0.50,0.75]))
print('Correlation matrix: ',df['Point'].corr(df['Point']))
print('describe() function')
print(df.describe())
'''
#Data Grouping and Aggregation:
'''
import pandas as pd 
df = pd.DataFrame({
'Student': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru',
'Can', 'Deniz', 'Gizem',
'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül',
'Kadir', 'İrem', 'Ozan'],
'Lesson': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik'],
'Point': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83,
94, 81, 84, 90]
})   
lesson_groups = df.groupby('Lesson')
average = lesson_groups['Point'].mean()
print('Average point: ',average)
minimum_point = lesson_groups['Point'].min()
print('Minimum point:',minimum_point)
maximum_point = lesson_groups['Point'].max()
print('Maximum point: ',maximum_point)
'''
#Data Sorting and Filtering:
'''
import pandas as pd 
df = pd.DataFrame({
'Student': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet', 'Aylin', 'Mustafa', 'Ebru',
'Can', 'Deniz', 'Gizem',
'İbrahim', 'Elif', 'Burak', 'Fatma', 'Emre', 'Ceren', 'Gül',
'Kadir', 'İrem', 'Ozan'],
'Lesson': ['Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya', 'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik', 'Kimya',
'Matematik', 'Fizik'],
'Point': [90, 85, 95, 75, 80, 92, 87, 88, 93, 82, 79, 91, 86, 89, 78, 83,
94, 81, 84, 90]
})    
sorted_data = df.sort_values(by='Point',ascending=False)
print('Sorted data: ',sorted_data)
mathematics_data = df[df['Lesson'] == 'Matematik']
print('Mathematics data: ',mathematics_data)
high_grades = df[df['Point'] > 85]
print('High grades: ',high_grades)
'''
#Joining Across Data Frames and Working with Joined Data
'''
import pandas as pd
df1 = pd.DataFrame({'Student':['Ali','Ayşe','Mehmet','Ahmet'],'Lesson':['Matematik','Fizik','Kimya','Matematik'],'Point':[90,85,95,75]})
df2 = pd.DataFrame({'Student': ['Ali', 'Ayşe', 'Mehmet', 'Ahmet'],
'Year': [18, 17, 19, 16],
'Gender': ['Erkek', 'Kadın', 'Erkek', 'Erkek']})
merge_df = pd.merge(df1, df2, on='Student')
math_lesson_takers = merge_df[merge_df['Lesson'] == 'Matematik']
print("Students Taking Mathematics Lessons:")
print(math_lesson_takers)
'''
#Multi-Indexing and Multi-Level Data Frames:
import pandas as pd
#Create the dataset
data = {'Şehir': ['İstanbul', 'İstanbul', 'İstanbul', 'Ankara', 'Ankara',
'Ankara'],
'Bölge': ['Avrupa', 'Avrupa', 'Anadolu', 'Anadolu', 'Avrupa',
'Anadolu'],
'Mevsim': ['Yaz', 'Kış', 'İlkbahar', 'Kış', 'Yaz', 'İlkbahar'],
'Sıcaklık': [30, 10, 20, 5, 25, 15]}
#Crate the data farame
df = pd.DataFrame(data)
#Set columns as indexes for multiple indexing
df.set_index(['Şehir', 'Bölge', 'Mevsim'], inplace=True)
#View a multilevel data frame
print(df)