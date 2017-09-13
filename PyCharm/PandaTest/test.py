__author__ = 'rjilani'

import pandas as pd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd


pd.set_option('max_columns', 50)

cols = ['num', 'game', 'date', 'team', 'home_away', 'opponent',
        'result', 'quarter', 'distance', 'receiver', 'score_before',
        'score_after']
no_headers = pd.read_csv('./data/peyton-passing-TDs-2012.csv', sep=',', header=None,
                         names=cols)
#print no_headers.head()

no_headers.to_excel('./data/test.xls', index =False)

football = pd.read_excel('./data/test.xls', 'Sheet1')
#print football


d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))

df = df.cumsum()

plt.figure(); df.plot();


