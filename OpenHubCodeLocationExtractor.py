#!/usr/bin/python

import csv
import sys
import requests
from HTMLParser import HTMLParser

project = ""

class MyHTMLParser(HTMLParser):
    foundBlock = False

    foundCodeLocation = False
    codeLocation = ""

    tdCounter = 0

    def handle_starttag(self, tag, attrs):
        if self.foundBlock and tag == 'td' and len(attrs) > 0 and attrs[0][1] == "col-md-4":
            self.foundCodeLocation = True

        elif tag == 'tr' and len(attrs) > 0 and attrs[0][0] == "class":
            self.foundBlock = True


    def handle_data(self, data):
        if self.foundCodeLocation and self.codeLocation == "":
            self.codeLocation = data


    def handle_endtag(self, tag):
        if tag == 'tr' and self.foundBlock:
            #Final output
            print(project + "|" + self.codeLocation)
            self.foundBlock = False
            self.CodeLocation = ""

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

