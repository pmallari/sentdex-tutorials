import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
			 'Visitors':[43, 54, 34, 45, 64, 34],
			 'Bounce_Rate':[65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)

#print(df)						prints all data
#print(df.head())				prints first five
#print(df.tail())				prints last five
#print(df.tail(2))				prints last 2

# print(df.set_index('Day'))	print set with 'Day' as index
# print(df.head())				print original dataset

# df2 = df.set_index('Day')		create new dataset with 'Day' as index
# print(df2.head())				print first five of new dataset

# print(df['Visitors'])			print visitors column
# print(df.Visitors)			another way to print

# print(df[['Bounce_Rate','Visitors']])
# print(np.array(df[['Bounce_Rate','Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate','Visitors']]))		#Convert DataFrame to numpy
print(df2)