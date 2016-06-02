import sys
sys.path.append('../utils/')
from CSVUtil import CSVUtil

import gspread
from oauth2client.service_account import ServiceAccountCredentials

# ------------ AUX FUNCTIONS -----------

# ------------ GOOGLE SPREAD SHEETS ------------
print 'Connecting to Google sheets...'
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('conf/sheet_conf.json', scope)
gc = gspread.authorize(credentials)

sh = gc.open("Planilha das notas - automatizada")
main_worksheet = sh.get_worksheet(0)
late_worksheet = sh.get_worksheet(1)
print 'Done!'

# ----------- GETTING USERS ---------------
print 'Getting users...'
users = [e for e in main_worksheet.col_values(2) if e != '']
users = users[1:] # removing 'title' of column
users = [(users[i], i + 2) for i in xrange(len(users))] # + 1 because of the title

print 'Users:', users

# ----------- GETTING LISTS  ----------------
print 'Getting lists...'
# Lists will have the list name and the column number
lists = [e for e in main_worksheet.row_values(1) if 'lista' in e]
lists = [(lists[i], i + 3) for i in xrange(len(lists))] # + 3 because of the name and user column
print 'Lists:', lists

# ----------- GETTING LATE PROBLEMS COLUMN -------

late_column = lists[len(lists)-1][1] + 1 #late column comes after the last list 

# ------------ UPDATE LATE COLUMN ----------------
print 'Updating late column from main sheet..'
for l in lists:
    for u in users:
        diff = int(late_worksheet.cell(u[1], l[1]).value) - int(main_worksheet.cell(u[1], l[1]).value)
        main_worksheet.update_cell(u[1], late_column, max(0, diff)) 
