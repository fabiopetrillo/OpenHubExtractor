#!/usr/bin/python

import csv
import sys
import requests
from HTMLParser import HTMLParser

# Line command CSV file argument
projectDataFile = sys.argv[1]

database = {}

def findTriplets(languages):
    if len(languages) >= 3:

        i = 0
        first = languages[i]
        middle = languages[i+1]
        last = languages[i+2]
        #print(first + "/" + middle + "/" + last)

        if database.has_key( first + "/" + middle + "/" + last):
            database[first + "/" + middle + "/" + last] = database[first + "/" + middle + "/" + last] + 1
        elif database.has_key(first + "/" + last + "/" + middle):
            database[first + "/" + last + "/" + middle] = database[first + "/" + last + "/" + middle] + 1
            #print(first + "/" + last + "/" + middle , database[first + "/" + last + "/" + middle])

        elif database.has_key(middle + "/" + first + "/" + last):
            database[middle + "/" + first + "/" + last] = database[middle + "/" + first + "/" + last] + 1
            #print(middle + "/" + first + "/" + last , database[middle + "/" + first + "/" + last])
        elif database.has_key(middle + "/" + last + "/" + first):
            database[middle + "/" + last + "/" + first] = database[middle + "/" + last + "/" + first] + 1

        elif database.has_key(last + "/" + first + "/" + middle):
            database[last + "/" + first + "/" + middle] = database[last + "/" + first + "/" + middle] + 1
        elif database.has_key(last + "/" + middle + "/" + first):
            database[last + "/" + middle + "/" + first] = database[last + "/" + middle + "/" + first] + 1
        else:
            database[first + "/" + middle + "/" + last] = 1



with open(projectDataFile, 'rU') as f:
    freader = csv.reader(f, delimiter = '|', quoting=csv.QUOTE_NONE)

    project = ""
    projectLanguages = []
    for row in freader:
        if project != row[0]:
           # print(project,projectLanguages)
            findTriplets(projectLanguages)
            project = row[0]
            projectLanguages = []

        projectLanguages.append(row[1])

print("Triplets,Occurrences")

for key, value in sorted(database.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print("{0}, {1}".format(key, value))