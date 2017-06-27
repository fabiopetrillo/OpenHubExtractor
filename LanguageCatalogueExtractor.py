#!/usr/bin/python

import csv
import sys
import requests
from HTMLParser import HTMLParser


project = ""
languages = set()

class MyHTMLParser(HTMLParser):
    foundBlock = False
    foundLanguage = False
    foundPercentage = False

    language = ""
    percentage = -1

    tdCounter = 0

    def handle_starttag(self, tag, attrs):
        if self.foundBlock and tag == 'a':
            self.foundLanguage = True
        elif tag == 'tr' and len(attrs) > 0 and attrs[0][0] == "class":
            self.foundBlock = True
        elif tag == 'span' and len(attrs) > 0 and attrs[0][1] == "pull-right":
            self.foundPercentage = True

    def handle_data(self, data):
        if self.foundLanguage and self.language == "":
            self.language = data
            self.foundLanguage = False


        if self.foundPercentage:
            self.foundPercentage = False
            self.percentage = data.replace("%","").strip()


    def handle_endtag(self, tag):
        if tag == 'tr' and self.foundBlock:
            #Final output
            if float(self.percentage) >= 0.5:
                  languages.add(self.language)
            self.foundBlock = False
            self.language = ""
            self.percentage = -1

        #if tag == 'html':
        #    print languages


#OpenHub main URL
URL = "https://www.openhub.net/p/{0}/analyses/latest/languages_summary"

# Line command CSV file argument
file = sys.argv[1]

with open(file, 'rU') as f:
    freader = csv.reader(f, delimiter = ',', quoting=csv.QUOTE_NONE)
    for row in freader:
        project = row[0]

        resp = requests.get(url=URL.format(project))
        parser = MyHTMLParser()
        parser.feed(resp.text)

    for language in languages:
        print language

