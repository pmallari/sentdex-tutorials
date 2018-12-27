import quandl
import pandas as pd

api_key = open('quandlapikey.txt', 'r').read()
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())

#Gets every dataframe in html website
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#list of dataframes
#print(fiddy_states)

#dataframe
#print(fiddy_states[0])

#dataframe column
#print(fiddy_states[0][1])

for abbv in fiddy_states[0][1][1:]:
	print("FMAC/HPI_"+str(abbv))

