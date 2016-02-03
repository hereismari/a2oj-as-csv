from server.web import *
from server.parseText import *

con = Connector('http://a2oj.com/standings?ID=23044')

result = con.read()

f = open('output', 'ab')
f.write(result)
f.close()


#parser = ParseText()

#parser.feed(con.read())
#parser.close()

#result = parser.getResult()
#for item in result:
#    print item
