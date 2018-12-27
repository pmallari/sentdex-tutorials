import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


# Not necessary, I just do this so I do not show my API key.burned house
api_key = open('quandlapikey.txt','r').read()


def state_list():
	fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return fiddy_states[0][1][1:]

def grab_inital_state_data():
	states = state_list()
	main_df = pd.DataFrame()

	for abbv in states:
	    #print(abbv)
	    query = "FMAC/HPI_"+str(abbv)
	    df = quandl.get(query, authtoken=api_key)
	    df = df.drop(labels = 'NSA Value', axis=1)
	    df.columns=[abbv]
	    df[abbv] = ((df[abbv] - df[abbv][0]) / df[abbv][0]) * 100
	    if main_df.empty:
	    	main_df = df
	    else:
	    	main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('pickle.pickle', 'wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

#Get total average for entire country
def HPI_Benchmark():
	df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
	df = df.drop(labels = 'NSA Value', axis=1)
	df.columns=['USA']
	df["USA"] = ((df["USA"] - df["USA"][0]) / df["USA"][0]) * 100
	return df

# grab_inital_state_data()

# fig = plt.figure()
# ax1 = plt.subplot2grid((1,1), (0,0))

HPI_data = pd.read_pickle('pickle.pickle')
# benchmark = HPI_Benchmark()

# HPI_data.plot(ax = ax1)
# benchmark.plot(ax=ax1, color = 'k', linewidth = 10)

# plt.legend().remove()
# plt.show()

HPI_State_Correlation = HPI_data.corr()

print(HPI_State_Correlation.describe())

# HPI_data['TX2'] = HPI_data['TX NSA Value'] * 2
# print(HPI_data[['TX NSA Value','TX2']])