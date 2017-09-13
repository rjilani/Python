__author__ = 'rjilani'


import pandas as pd
from pandas import DataFrame, Series

complains = pd.read_csv('C:\Projects\scala_project\Data\complain_database\Consumer_Complaints.csv',
                        index_col='Complaint ID', parse_dates=['Date received','Date sent to company'], sep=',', low_memory=False)

# print complains['Date received'][:2]

print len(complains)

company = complains['Company'].groupby(level=0).sum()

print company

# for comp in company:
#     print comp



# grouped = complains.groupby('Company')
#
# print grouped.ngroups

# def print_groups (groupobject):
#     for name, group in groupobject:
#         print (name)
#         print (group)


# print_groups(grouped)

# print grouped.size()

# print grouped.get_group('Ocwen')

