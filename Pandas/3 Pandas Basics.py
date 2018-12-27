import pandas as pd 
import numpy as np 

Import csv files through pandas
df = pd.read_csv("ZILLOW-CO1781_MLPAH.csv")
df.set_index('Date', inplace = True)
print(df.head())
df.to_csv('newcsv2.csv')

#Read new csv
df = pd.read_csv('newcsv2.csv')
print(df.head())

#Dataframe with no index
df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

#Define column names
df.columns = ['Austin_HPI']
print(df.head())

#Save csv file without header
df.to_csv('newcsv3.csv')
df.to_csv('newcsv4.csv', header = False)

#Import csv file without header and automatically add headers
df = pd.read_csv('newcsv4.csv', names = ['Date', 'Austin_HPI'])
print(df.head())

#Convert to html
df.to_html('example.html')

#Name csv file import
df = pd.read_csv('newcsv4.csv', names = ['Date','Austin_HPI'])
print(df.head())

#Rename dataframe columns in place
df.rename(columns = {'Austin_HPI': '77006_HPI'}, inplace = True)
print(df.head())