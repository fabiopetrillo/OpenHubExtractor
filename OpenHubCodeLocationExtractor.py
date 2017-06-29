#!/usr/bin/python

import csv
import sys
import requests
from HTMLParser import HTMLParser

project = ""

class MyHTMLParser(HTMLParser):

    foundCodeLocation = False
    codeLocation = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'td' and len(attrs) > 0 and attrs[0][1] == "col-md-4":
            self.foundCodeLocation = True


    def handle_data(self, data):
        if self.foundCodeLocation and self.codeLocation == "":
            self.codeLocation = data
            print(project + "|" + self.codeLocation)


#OpenHub main URL
URL = "https://www.openhub.net/p/{0}/enlistments"
# Line command CSV file argument
projectFile = sys.argv[1]


languages = set()

print("Project|CodeLocation")

with open(projectFile, 'rU') as f:
    freader = csv.reader(f, delimiter = ',', quoting=csv.QUOTE_NONE)
    for row in freader:
        project = row[0]

        resp = requests.get(url=URL.format(project))
        parser = MyHTMLParser()
        parser.feed(resp.text)

