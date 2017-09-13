import json

path = 'C:/Projects/datascience/data/factbook.json/world/xx.json'

# records = [json.load(line) for line in open(path)]
#
# for line in open(path):
#     print line

with open(path) as json_file:
    json_data = json.load(json_file)
    print json_data['Transportation']