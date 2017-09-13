import numpy as np

import time


data2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12]]

arr2 = np.array(data2)

# print arr2
#
# print arr2.shape

print arr2[1][0]

print np.zeros(10, dtype=int)

arr3 = arr2 * 3

arr2[1] = [1,2,3,4]

print (arr2[arr2.argmin()])

print arr2.sort()