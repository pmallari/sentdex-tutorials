import quandl
import pandas as pd
import pickle

# Not necessary, I just do this so I do not show my API key.
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
	    df.rename(columns={'NSA Value':str(abbv) + ' NSA Value' , 'SA Value' : str(abbv) + ' SA Value'}, inplace=True)

	    if main_df.empty:
	    	main_df = df
	    else:
	    	main_df = main_df.join(df)

	print(main_df.head())

	pickle_out = open('fiddy_states.pickle', 'wb')
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

#grab_inital_state_data()

#Python default pickle
pickle_in = open('fiddy_states.pickle', 'rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)

HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)