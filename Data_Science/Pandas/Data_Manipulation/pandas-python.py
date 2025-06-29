"""#################################Pandas Notes###############################################"""

import numpy as np
import pandas as pd
from numpy import random

labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array(my_list)

series = pd.Series(data=arr, index=labels) #create a series by passing in an iterable as the first arg, second arg as the label
print(arr)
d = {'a': 10, 'b': 20, 'c': 30}

series_dict = pd.Series(d) #create a series by passing in a dict where the keys are label and values are values

series1 = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series(data=[10, 20, 30, 40, 50], index=['a', 'b', 'c', 'y', 'z'])

series3 = series1 + series2 #series can be added for the same indexes, for different indexes NaN

#dataframe is a colelction of series
df = pd.DataFrame(random.randint(1, 100, (5, 4)), index=['A', 'B', 'C', 'D', 'E'], columns=['W', 'X', 'Y', 'Z']) #arg1 = data, arg2 = row labels, arg3 = col labels

df.info() #gives series info

df.head() #gives the number of rows required, default 5

df_col = df['W'] #select one col from df

df_multiple_cols = df[['W', 'Z']] #select multiple cols from df

df['new_using_iterable'] = [1, 2, 3, 4, 5] #create new col of the df using a new iterable

df['new_using_existing'] = df['X'] + df['Y'] #create new col of the df using the existing cols

df.drop('new_using_iterable', axis=1) #to delete a col set axis to 1, to delete row set axis to 0

#the updates to the df are in its copy and do not reflect in the og df

df.drop('new_using_iterable', axis=1, inplace=True) #for changes to reflect set inplace to True
df.drop('new_using_existing', axis=1, inplace=True)

using_label = df.loc['A'] #to select row using label

using_row_number = df.iloc[3] #to select row using row number

booldf = df > 50 #create a new df with the values for the given cond holding True else False

new_df = df[booldf] #create a new df where the values of True are shown else NaN

sliced_df = df[df['W'] > 40] #create a new df where the rows are shown whose col('W') value fulfils cond

multiple_selections_df = df[df['W']> 40][['X', 'Y']] #create a new df with only the given cols('X', 'Y') where the value of given col('W') value fulfils the cond

df.reset_index() #resets to the default index

df["index"] = "AB CD EF GH IJ".split()
df.set_index("index") #change the index to the col passed

and_cond = df[(df['W'] > 40) & (df['Y'] < 80)] #create a ddf with val of col1 AND col2 fulfilling the given conds

or_cond = df[(df['W'] > 40) | (df['Y'] < 20)] #create a ddf with val of col1 OR col2 fulfilling the given conds

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

ndf = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])

ndf_1level = ndf.loc["G1"] #go 1 level in the df

df_2level = ndf.loc["G1"].loc[1] #go 2 level in the df

df_3level = ndf.loc["G1"].loc[1]['B'] #go 3 level in the df

#df with given level and its name
#df_xs = ndf.xs(1, level="Num")

df_dict = pd.DataFrame({'A':[1, 2, np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}) #df from dict

df_dict.dropna() #drop the rows containing NaN

df_dict.dropna(axis=1) #drop the cols containing NaN

df_dict.dropna(thresh=2) #drop the rows containing val(2) or more NaN

df_dict.fillna(value="Fill") #Fill the NaN values with value

df_dict['A'].fillna(value="Fill") #Fill the NaN values with value for given clo

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

data_frame = pd.DataFrame(data)

group_by_df = data_frame.groupby("Company") #group the same values of the given col

data_frame.groupby("Company").describe() #gives basic data about the df like count, sum, mean, min, etc

data_frame.transpose() #Transpose the given df

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

concate_on_rows = pd.concat([df1, df2, df3]) #concate the rows one below the other

concate_on_cols = pd.concat([df1, df2, df3], axis=1) #concate the cols one below the other

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})


merge = pd.merge(left, right, how="inner", on="key") #merge the df's given on the basis of the col given in 'on' attribute, 'how' attribute is the type of join used

left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

join = left.join(right) #join the two clos with different indexes. 'how' attribute is the type of join

df['W'].unique() #show the unique vals

df['W'].nunique() #show the no. unique vals

df['W'].value_counts() #show the unique vals and their count

df.apply(len) #apply a function the entire col

df['W'].sum() #sum of the entire col

df.sort_values(by='X') #sort the vals acc to the values in given col('X')

df.isnull() #df of the vals where the val is NaN

df.dropna() #drop the rows with NaN

df_cols = df.columns #names of all the cols

df_index = df.index #names of all the index

Data_Frame = pd.read_csv("example") #read a csv

Data_Frame.to_csv("New_CSV", index=False) #write to a csv. index True to save teh old df index
print(Data_Frame)
