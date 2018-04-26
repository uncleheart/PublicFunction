#
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 800))
# display.start()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "http://www.dangniao.com/mh/22996/392953.html"
browser = webdriver.PhantomJS("/root/phantomjs-2.1.1-linux-i686/bin/phantomjs")
browser.get(url)