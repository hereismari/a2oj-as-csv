#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.webConnection import *
from utils.HTMLgetter import *
from utils.CSVUtil import *
import sys

# ------------ GLOBAL CONSTANTS --------------

RANK_INDEX = 0
COUNTRY_INDEX = 1 
SOLVED_INDEX = 2

MAXIMUM_ARGV_LEN = 4
MINIMUM_ARGV_LEN = 2
def howToUse():
    print '$python runApp.py <ID of the standings> -o <name/path of the output>'
    print 'If  -o parameter is not passed the output name will be the name of the standings'

# ------------ GETTING INPUT ---------------

html = 'http://a2oj.com/standings?ID='

if len(sys.argv) == MAXIMUM_ARGV_LEN and sys.argv[2] != '-o':
    howToUse()
    sys.exit(1)
elif len(sys.argv) == MAXIMUM_ARGV_LEN:
    html += sys.argv[1]
    output_name = sys.argv[3] 
elif len(sys.argv) == MINIMUM_ARGV_LEN:
    html += sys.argv[1]
    output_name = ''
else:
    howToUse()
    sys.exit(1)

# -------------- SETTING OBJECTS --------------

con = Connector(html)
html_as_text = con.read()

root = lxml.html.fromstring(html_as_text)
getter = HTMLgetter(html_as_text)

csv_util = CSVUtil()

if output_name == '': output_name = getter.getStandingsName() + '.csv'

# -------------- GETTING INFORMATION --------------

usernames = getter.getUsernames()
problems = getter.getProblems()

users_info = []
for i in xrange(len(usernames)):
    users_info.append(getter.getUserInfo(i, len(problems)))

total_sub, total_acc = getter.getProblemsInfo()

# ------------ CREATING LIST OF LISTS TO CONVERT EASILY TO CSV ----------

result = [[0] * (len(problems) + 4) for i in xrange(len(usernames) + 1)] # + 1 -> HEADER

result[0] = ['username', 'ranking', 'country', 'number of solved problems']
for problem in problems:
    result[0].append(problem)

print result

for i in xrange(0, len(usernames)):
    result[i+1][0] = usernames[i] # +1 -> HEADER

for i in xrange(len(users_info)):
    result[i+1][RANK_INDEX + 1] = users_info[i][RANK_INDEX]
    result[i+1][COUNTRY_INDEX + 1] = users_info[i][COUNTRY_INDEX]
    result[i+1][SOLVED_INDEX + 1] = users_info[i][SOLVED_INDEX]
    
    # Start problems information
    count = SOLVED_INDEX + 2
    for problem in problems:
        result[i+1][count] = users_info[i][count-1]
        count += 1

print result

# ------- SAVING IN CSV ---------

csv_util.saveAsCSV(output_name, result)

