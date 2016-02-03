import HTMLParser

class ParseText(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.result = []

    def handle_data(self, data):
        self.result.append(data)
   
    def getResult(self):
       return self.result
