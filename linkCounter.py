import re
import mechanize
import subprocess

br = mechanize.Browser()

year = 2008
for year in range (2008, 2015):
    "Looking up " + str(year)
    linkToResults = "http://www.joyoftournaments.com/sc/state/" + str(year)
    br.open(linkToResults)
    year += 1

    numberOfResultsAvailable = 0
    for link in br.links():
        print "Doing results number " + str(numberOfResultsAvailable) + " " + link.text
        event = link.url
        results = "http://www.joyoftournaments.com/sc/state/2008/" + event
        subprocess.call("wget " + results, shell=True)
        numberOfResultsAvailable += 1
