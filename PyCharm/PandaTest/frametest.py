import numpy as np
import pandas as pd


msft = pd.read_csv("data/NST-EST2015-popchg2010_2015.csv", usecols = ['NAME','POPESTIMATE2015'], index_col=['NAME'])

# print msft.shape
# print msft.dtypes
# a = msft.head()
#
# msft.to_csv("data/states_pop.csv")

print (msft['POPESTIMATE2015'].argmax() + ' ' + str(msft['POPESTIMATE2015'].max()) )

print (msft['POPESTIMATE2015'].argmin() + ' ' + str(msft['POPESTIMATE2015'].min()) )