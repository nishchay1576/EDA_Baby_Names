'''
Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made 
    available data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip)  
    
    Read data from all the year files starting from 1880 to 2010 and year > 2013, 
    add an extra column named as year that contains year of that 
    particular data. 
    
    Concatinate all the data to form single dataframe 
    using pandas concat method.
    
    Display the top 5 male and female baby names of 2010.
    
    Calculate sum of the births column by sex as the total number of births 
    in that year(use pandas groupby method).
    
    Plot the results of the above activity to show total births 
    by sex and year.
'''
    
import re
import pandas as pd
from glob import glob

filenames = glob('*.txt')

dataframe = []

for file in filenames:
    temp_df = pd.read_csv(file, names = ['name','sex','count'])

    year = int(re.findall('\d\d\d\d',file)[0])
    if (year >=2010 and year<=2013):
        break
    temp_df['year'] = year
    dataframe.append(temp_df)
    

finaldf = pd.concat(dataframe,axis=0,ignore_index=True)
topMF_2010 = finaldf[finaldf['year'] == 2000]

female_names = topMF_2010[topMF_2010['sex'] == 'F']
female_names_sort_by_count = female_names.sort_values('count',ascending=False,ignore_index=True)
print(female_names_sort_by_count['name'][0:5])

male_names = topMF_2010[topMF_2010['sex'] == 'M']
male_names_sort_by_count = male_names.sort_values('count',ascending=False,ignore_index=True)
print(male_names_sort_by_count['name'][0:5])

grouped_multiple = finaldf.groupby(['year', 'sex']).agg({'count': ['sum']})
print(grouped_multiple)

grouped_multiple.plot(kind='bar')

grouped_multiple[0:10].plot(kind='bar')


