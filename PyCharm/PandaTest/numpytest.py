import numpy as np

from pandas import Series, DataFrame

import pandas as pd

obj = Series([4, 7, -5, 3])

print obj[2]

print obj.index[0]

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

print ('b' in obj2)