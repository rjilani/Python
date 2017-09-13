__author__ = 'rjilani'

from pandas_datareader import DataReader
from datetime import date
from dateutil.relativedelta import relativedelta
import pandas as pd
import matplotlib as plt



from matplotlib import pyplot as plt

# read the last three months of data for GOOG

df = pd.read_csv('./data/listofstocks.csv',usecols=['Symbols'])

NOOFMONTHS=-168

for index, row in df.iterrows():
    print row[0]
    stockdetail = DataReader(row[0], "yahoo",
    date.today() +
    relativedelta(months=NOOFMONTHS))

    frame = [stockdetail.head(), stockdetail.tail()]
    result = pd.concat(frame)

    print result

    high = (list(result[result.columns[0]]))
    dates = list(result.index)

    # print dates
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.plot(dates, high)
    # plt.show()
    plt.savefig("./data/stock/"+ row[0]+ ".png")


    result.to_csv("./data/stock/"+ row[0]+ ".csv", sep=',')
    # ax = result.plot()
    # fig = ax.get_figure()
    # fig.savefig("./data/stock/"+ row[0]+ ".png")










