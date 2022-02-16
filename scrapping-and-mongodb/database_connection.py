import json
import pymongo
import pandas as pd
import pprint
import csv
import sys, getopt, pprint

from sympy import limit

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())
mydb = myclient["Prof_Info"]
myCol=mydb['prof_data']
query={"expertise":{"$regex":'Fluid Dynamics'}}
mydoc = myCol.find(query,{ "_id": 0, "name": 1, "expertise": 1 }).limit(3)

for x in mydoc:
  val=str(pprint.pprint(x))
  print(val)

# csvfile = open('profile_exps.csv', 'r',encoding='utf-8')
# reader = csv.DictReader( csvfile )
# header=['name','expertise','phone','about']


# for each in reader:
#     row={}
#     for field in header:
#         row[field]=each[field]

#     myCol.insert_one(row)


