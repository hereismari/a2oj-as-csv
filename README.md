# a2oj As CSV

Python script that takes an [a2oj](http://a2oj.com/) standing and returns a csv with the submissions information.
This was tested and is woking with: Ubuntu 16.4 and Chrome.

In this repository there is also an app to automatic update a sheet at [Google Sheets](https://www.google.com/sheets/about/) based on the `runApp.py` result.
Thank you so much [gspread](https://github.com/burnash/gspread) people :smile:

# What will I need in order to run it?

Some python libs:
- selenium
- cssselect
- pyvirtualdisplay
- lxml

And some internet connection will help haha :smile: (but really, you'll need it). Algo I'm using Chrome as browser, you can change it if you want, just change the webdriver line in [this file](https://github.com/mari-linhares/a2oj-as-csv/blob/master/utils/webConnection.py).

# Ok, but how do I run it?

Run it on shell:

`$python runApp.py <ID of the standings> -o <name/path of the output>`

If the name/path of the output isn't explicit the output will be `<Standings name>.csv`

This will give you a full table almost like a2oj it self.

## How is the output file?

Username | Ranking | Country | Number of Solved Problems| P1 - url | P2 - url | P3 - url | ... | PN - url|
-------- | --------| --------| -------------------------| ---------| ---------| ---------| ----| --------|
user1    |    1    |  Brazil |              3           |     1    |     1    |     1    | ... |     0/0 |
user2    |    2    |  India  |              2           |     0/0  |     0/0  |     1    | ... |     1   |
user3    |    3    |  Russia |              2           |     0/8  |     1    |     0/0  | ... |     1   |
...      |    ...  |  Brazil |              1           |     0/0  |     1    |     0/7  | ... |     0/54|
usern    |    n    |  Brazil |              0           |     0/100|     0/0  |     0/0  | ... |     0/0 |
