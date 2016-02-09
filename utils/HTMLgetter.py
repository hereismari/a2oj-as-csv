import lxml.html

class HTMLgetter():

    def __init__(self, html):
        self.html = html
        self.root = lxml.html.fromstring(html)

    def getStandingsName(self):
        for element in self.root.cssselect('b a'):
            return element.text

    def getUsernames(self):
        
        users = []
        for element in self.root.cssselect('tr .actualTable td .normal'):
            if 'Username' in element.get('href'):
                users.append(element.text)
            
        print 'The usernames are:', users
        return users
    
    def getProblems(self):
        
        problems = []
        
        # The css bellow returns the usernames followed by the problems
        # So we have to ignore the usernames and take the rest of the info
        for element in self.root.cssselect('tr .actualTable td .normal'):
            if 'Username' in element.get('href') or 'submission' in element.get('href'):
                continue
            else:
                problems.append(element.text + ' ' + element.get('href'))

        print 'The problems are:', problems
        return problems
    
    def getUserInfo(self, index, number_of_problems):
        
        info = []

        # the position in the cssselect
        # each user will have the result of each problem associated
        # (number_of_problmes) + rank_info, time_info, country_info,
        # and number of problems resolved + null td
        position = index * (number_of_problems + 5)
        
        count = 0
        for element in self.root.cssselect('tr .actualTable td'):
            if count >= position + number_of_problems + 5: break # info finished, you can go
            if count >= position:
                info.append(element.text)
            count += 1

        info.pop(1) # removing NULL td
        info.pop(3) # removing time info, this information in particular
                       # doesn't interest me

        # solved problems will have None value
        # as I said I'm not interested in the time
        # and in this case neither in the number of tries.
        # So if it was solved (== None) I put an "1".
        info = ['1' if element is None else element for element in info]

        # rank, country, number of solved problems, p1, p2, ..., pn 
        return info

    def getProblemsInfo(self):

        submitted = []
        accepted = []
        
        #Submitted come before Accepted
        startSubmitted = False
        startAccepted = False

        for element in self.root.cssselect('tr .actualTable td'):
            
            if element.text is None: continue    
            elif 'Total Submitted' == element.text:
                startSubmitted = True
            elif 'First Accepted' == element.text:
                startSubmitted = False
            elif 'Total Accepted' == element.text:
                startAccepted = True
            elif startSubmitted:
                submitted.append(element.text)
            elif startAccepted:
                accepted.append(element.text)

        return submitted, accepted
