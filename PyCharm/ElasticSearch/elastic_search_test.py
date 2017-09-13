__author__ = 'rjilani'

import requests
import json
import elasticsearch
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# i = 1
# while i< 25:
#     if (i != 17):
#         r = requests.get('http://swapi.co/api/people/'+ str(i))
#         es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#         print(i)
#     #es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
#
#     i=i+1
#     print (r.text)

people = es.get(index='sw', doc_type='people', id=5)

people = es.search(index="sw", body={"query": {"match": {'name':'Darth Vader'}}})

people = es.search(index="sw", body={"query": {"prefix" : { "name" : "lu" }}})

people = es.search(index="sw", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": "jaba", "max_query_terms":5}}}})

print people