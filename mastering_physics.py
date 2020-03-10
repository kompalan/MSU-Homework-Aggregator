#### getting the mastering physics data #####

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import urllib.request

browser = webdriver.Chrome(r'C:\Users\eshan dixit\Downloads\chromedriver_win32 (1)\chromedriver.exe')

username = 'dixitesh@msu.edu'
password = 'Likapuncha18'
course_no = 'fisher95612'

try:
    browser.get('''https://pi.pearsoned.com/v1/piapi/piui/signin?client_id=dN4bOBG0sGO9c9HADrifwQeqma5vjREy&okurl=https:%2F%2Fportal.mypearson.com%2Fcourse-home&siteid=8313''')
    
    sleep(2)
    
    Username = browser.find_element_by_name('username').send_keys(username)
    
    sleep(0.5)
    
    Password = browser.find_element_by_name('password')
    Password.send_keys(password)
    
    Password.submit()
    
    sleep(4)
    
    try:
        go_to_course = browser.find_element_by_xpath('//*[@id="tab-outer-container"]/div/course-card-container/div/div[4]/div/div[1]/div/div/div[2]/ul/li/card-view/ng-include/div/div/div/div[2]/div[1]/div[3]/div').click()
        
        sleep(4)
        
        try:    
            subject = browser.find_element_by_xpath('//*[@id="course-title"]/h1').text
            print(subject)
            
            sleep(5)
            
            # getting the assignments from the unordered list
            elements =  browser.find_elements_by_class_name('assignment-row')
            
            
            
        except:
            print(Exception)
          
    except:
        print("I couldn't get your course")

except:
    print("Oops, can't open the browser")