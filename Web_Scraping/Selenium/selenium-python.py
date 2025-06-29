from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#keep the webpage window on
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#load and open the webpage
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Green-Soul-Monster-Ultimate-Multi-Functional/dp/B085NPF8BK/ref=sr_1_1_sspa?crid=1EGCA6Y6BJKCG&dib=eyJ2IjoiMSJ9.mH-t44wCf0hdO3RbDbx5FNENt_fQ8aWuusEWUZlmz16-cV2s-3sYZZiUH_GA3TUzxnbidZqiaiyPRJJr2FEo7kXOifkjfmuan-7bmv8re9FPZ7jGWF-LM8_axBKGQeKpy96JrUreJXAn1GUFo2nqDdjcKfMamDQWesxmi5xJTc0WSvq-i33d5EKNs1TdU5hlzsYsVFZZ-Ps_b0xePbCzCplvxVdAu0un-UGCeedtB-QIUmBNJXf-YQ2_HxF1fU3L9YNoeOHIsfs_s57P7XVZe0kNOI1qqPltNi5RYV61SvE.jqffuCqIpPiv1lPZe80uQgFYFlAncqjVKEz4iVZ8SvQ&dib_tag=se&keywords=Gaming%2BChair&qid=1730294994&sprefix=gaming%2Bchair%2Caps%2C185&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")


#close the webpage. Only the active tab is closed
#driver.close()

#get the value specified for the given class
price = driver.find_element(By.CLASS_NAME, "a-price-whole")

#get tag name of the given element
tag_name = price.tag_name

#get attribute value of the given element
attribute = price.get_attribute("class")


"""
Locating elemnts by attribute, names, class or id can be tedious
The method that always works and is easy is XPath
XPath is the address of a tag in a HTML document
"""

#getting an element by XPath
search_bar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')

"""
The Keys class contains many constants which represent the special keys on our keyboard
"""
for i in range(20):
    #send_keys is used to emulate the keyboard typing. The key or text entered given as the input to the given element
    search_bar.send_keys(Keys.BACKSPACE)

search_bar.send_keys("Headphones", Keys.ENTER)


#open a link with mouse click
element_to_click = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span')
element_to_click.click()

time.sleep(10)

#close the entire browser
#driver.quit()