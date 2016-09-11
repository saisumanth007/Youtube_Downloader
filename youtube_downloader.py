from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

fp=webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "video/mp4")

display=Display(visible=0,size=(800,600))

title=raw_input("Enter the title of video to be downloaded: ")
print 'Connecting to the website ...'
#display.start()
driver=webdriver.Firefox(firefox_profile=fp)

# try:
# 	driver.get("https://www.youtube.com")
# 	print 'Connection established!'
# except:
# 	print 'No net connection'
driver.get("https://www.youtube.com")
print 'Connection successful'
time.sleep(5)

search=driver.find_element_by_xpath("//*[@id='masthead-search-term']")
search.send_keys(title.lower())
print 'Searching for the best match of the video ...'

submit=driver.find_element_by_xpath("//*[@id='search-btn']")
submit.click()
time.sleep(5)

url= driver.find_element_by_css_selector("ol.item-section > li:nth-child(4) a.yt-uix-tile-link").get_attribute('href')
new_url="https://www.ss"+url[12:]

main_window=driver.current_window_handle
htmlunit=driver.find_element_by_tag_name('html')



curWindowHndl = driver.current_window_handle
htmlunit.send_keys(Keys.CONTROL + 't'+Keys.CONTROL,new_url) 
htmlunit.send_keys(Keys.ENTER)
time.sleep(2) 
driver.switch_to_window(curWindowHndl)
print 'Attempting to Download ...'
time.sleep(20)


down=driver.find_element_by_css_selector("a.link-download")
down_link=down.get_attribute('href')
down.click()
print 'Download started ...'

time.sleep(5)
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL+'w') 
driver.switch_to_window(curWindowHndl)

time.sleep(120)

driver.quit()
#display.stop()