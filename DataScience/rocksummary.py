#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rjilani
#
# Created:     19/06/2015
# Copyright:   (c) rjilani 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import urllib2
import sys


def main():
    pass

if __name__ == '__main__':
    main()


target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []
for line in data:
#split on comma
    row = line.strip().split(",")
    print row
    xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[0])))