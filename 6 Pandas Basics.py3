import pandas as pd

# df1 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2001, 2002, 2003, 2004])

# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2005, 2006, 2007, 2008])

# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Unemployment':[7, 8, 9, 6],
#                     'Low_tier_HPI':[50, 52, 50, 53]},
#                    index = [2001, 2002, 2003, 2004])

# print(pd.merge(df1, df2, on='HPI'))
# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})

# #Merging based on year
# merged = pd.merge(df1, df3, on='Year')
# merged.set_index('Year', inplace=True)
# print(merged)

# #Merging based on index of left (df1)
# merged = pd.merge(df1, df3, on='Year', how = "left")
# merged.set_index('Year', inplace=True)
# print(merged)

# #Merging based on index of right (df3)
# merged = pd.merge(df1, df3, on='Year', how = "right")
# merged.set_index('Year', inplace=True)
# print(merged)

# #Merging based on index of inner (no NaN)
# merged = pd.merge(df1, df3, on='Year', how = "inner")
# merged.set_index('Year', inplace=True)
# print(merged)

# #Merging based on index of outer (all possible values)
merged = pd.merge(df1, df3, on='Year', how = "outer")
merged.set_index('Year', inplace=True)
print(merged)
