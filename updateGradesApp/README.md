
# Update grades

These are scripts to automatic update a google sheet containning information about ahmed-aly submissions (in specific students grades).
An example of the final result right [here](https://docs.google.com/spreadsheets/d/19_QdpZQ1PXhzI83qnb-_lMZhP3nNwHAtk0cnw3rdR6A/edit?usp=sharing).

**Important: to use this script the sheet mush have the same structure as the example and have a second sheet with the same template but different list names (can be seen in the link bellow) **

SHEET 1

Nome completo | ahmed-aly user  | lista1  | lista2  | ... | listan  | atrasadas | Número de questões | Nota    |
------------- | --------------- | ------- | ------- | --- | ------- | --------- | ------------------ | ------- |
user1         |    user1        |  0      |   3     | ... |     1   |     1     |                    |         |
user2         |    user2        |  1      |   2     | ... |     0   |     1     |                    |         |
user3         |    user3        |  4      |   2     | ... |     1   |     0     |                    |         |
...           |    ...          |  2      |   1     | ... |     1   |     7     |                    |         |
userm         |    userm        |  0      |   0     | ... |     0   |     0     |                    |         |

SHEET 2

Nome completo | ahmed-aly user  | lista1-r  | lista2-r  | ... | listan-r  | atrasadas | Número de questões | Nota    |
------------- | --------------- | --------- | --------- | --- | --------- | --------- | ------------------ | --------|
user1         |    user1        |  0        |   3       | ... |     1     |     1     |                    |         |
user2         |    user2        |  1        |   2       | ... |     0     |     1     |                    |         |
user3         |    user3        |  4        |   2       | ... |     1     |     0     |                    |         |
...           |    ...          |  2        |   1       | ... |     1     |     7     |                    |         |
userm         |    userm        |  0        |   0       | ... |     0     |     0     |                    |         |

## What do I need in order to run it?

  - Every column that is a contest in ahmed-aly(list) must have the word *lista* in it. And for every list lista1, lista2, ... listan must exist a file csv in the folder *lists* with the same name. 
  - install [gspread](https://github.com/burnash/gspread)
  - Obtain OAuth2 credentials from Google Developers Console (as especified in the gspread repository).
    You'll get a conf file and **must** put this file in the conf folder with the name `sheet_conf.json`!!!
  - Almost done! Now you'll have to give the email of your google developer account the permission to edit the sheet.
    (Just share with this email the sheet and give it write access)
    
## How to run?
  
  - execute the `updateAll.sh` and pass the sheet name as a parameter :smile:
    
    Example: `updateAll.sh grades`
  
