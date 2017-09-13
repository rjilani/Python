import pandas as pd

obj = pd.Series([4, 7, -5, 3], index = [1,2,3,4])

print obj[[1,2]]
