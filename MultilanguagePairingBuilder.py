#!/usr/bin/python

import csv
import sys
import requests
from HTMLParser import HTMLParser

# Line command CSV file argument
projectDataFile = sys.argv[1]

database = {}

def findPairs(languages):
    for i in range(len(languages)):
        pivot = languages[i]
        for j in range(len(languages)-i-1):
            j = j + i + 1
            if database.has_key(pivot + "/" + languages[j]):
                database[pivot + "/" + languages[j]] = database[pivot + "/" + languages[j]] + 1
            elif database.has_key(languages[j] + "/" + pivot):
                database[languages[j] + "/" + pivot] = database[languages[j] + "/" + pivot] + 1
            else:
                database[pivot + "/" + languages[j]] = 1
            #print(pivot + "/" + languages[j], database[pivot + "/" + languages[j]])



with open(projectDataFile, 'rU') as f:
    freader = csv.reader(f, delimiter = '|', quoting=csv.QUOTE_NONE)

    project = ""
    projectLanguages = []
    for row in freader:
        if project != row[0]:
            #print(project,projectLanguages)

            findPairs(projectLanguages)
            project = row[0]
            projectLanguages = []

        projectLanguages.append(row[1])

print("Pair,Occurrences")

for key, value in sorted(database.iteritems(), key=lambda (k,v): (v,k),reverse=True):
    print("{0}, {1}".format(key, value))