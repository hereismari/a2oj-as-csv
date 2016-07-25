import sys
import os.path
import os

sys.path.append('../utils/')

from CSVUtil import CSVUtil

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------ GETTING INPUT ----------
sheet_number = int(sys.argv[1]) # 0 main sheet, 1 late problems
sheet_name = sys.argv[2]

# ------------ AUX FUNCTIONS -----------

def getAhmedAlyID(cell):
    return  cell.input_value.split("ID=", 1)[1][0:5]

def getSolvedInfo(l, ahmed_aly_id):

    result = {}
    csv = CSVUtil()

    file_name = 'lists/' + l + '.csv'

    if not os.path.isfile(file_name):
        print "%s does not exist, I'll get this for you!" % file_name
        os.system('python ../runApp.py %s -o %s' % (ahmed_aly_id, file_name))
    else:
        ans = raw_input('File already exists (and probably the column was already setted), want to update column again? (y/n)')
        if ans == 'n': return (None, False)
    matrix_info = csv.openCSV(file_name)
    for i in xrange(1, len(matrix_info)):
        result[matrix_info[i][0]] = matrix_info[i][3]

    return (result, True)

# ------------ GOOGLE SPREAD SHEETS ------------

print 'Connecting to Google sheets ...'
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('conf/sheet_conf.json', scope)
gc = gspread.authorize(credentials)

sh = gc.open(sheet_name)
main_worksheet = sh.get_worksheet(sheet_number)
print 'Done!'

# ----------- GETTING USERS ---------------

print 'Getting users...'
users = [e for e in main_worksheet.col_values(2) if e != '']
users = users[1:] # removing 'title' of column
users = [(users[i], i + 2) for i in xrange(len(users))] # + 1 because of the title

print 'Users:', users

# ----------- GETTING LISTS  ----------------
# Lists will have the list name and the column number

print 'Getting lists...'
lists = [e for e in main_worksheet.row_values(1) if 'lista' in e]
lists = [(lists[i], i + 3, getAhmedAlyID(main_worksheet.cell(1, i+3))) for i in xrange(len(lists))] # + 3 because of the name and user column

print 'Lists:', lists

# ------------ UPDATE LISTS ----------------
print 'Updating lists in the sheet'
for l in lists:
    solved, update = getSolvedInfo(l[0], l[2])
    if update:
        for u in users:
            try:
                number_of_solved = solved[u[0]]
            except KeyError:
                number_of_solved = 0
            main_worksheet.update_cell(u[1], l[1], number_of_solved)
