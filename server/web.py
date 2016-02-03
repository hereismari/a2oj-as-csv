from selenium import webdriver

class Connector():

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Firefox()
        self.browser.get(url)
    def read(self):
        return self.browser.page_source

