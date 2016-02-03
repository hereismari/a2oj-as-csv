from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://a2oj.com/standings?ID=23044')
html_source = browser.page_source
print html_source
