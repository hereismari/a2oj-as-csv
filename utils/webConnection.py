from selenium import webdriver
from pyvirtualdisplay import Display

class Connector():

    def __init__(self, url):

        print 'Creating display...'
        self.display = Display(visible = 0, size = (800,600))
        self.display.start()
        
        self.url = url
        
        print 'Opening browser (Firefox) ...'
        self.browser = webdriver.Firefox()
        self.browser.get(url)
        print 'Saving page source...'
        self.page_source = self.browser.page_source
        
        print 'Success! Browser is being closed...'
        self.browser.quit()
        self.display.stop()

    def read(self):
        return self.page_source
