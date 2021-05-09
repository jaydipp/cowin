from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

path = 'D:/Tools/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)

driver.get('https://www.cowin.gov.in/home')
html = driver.page_source

pincode = 392001
pin_input= driver.find_element_by_id('mat-input-0')
pin_input.send_keys(pincode)

search_button = driver.find_element_by_class_name('pin-search-btn').click()

radio_button_18_plus = driver.find_element_by_id("flexRadioDefault1").click()

body_content = driver.find_element_by_css_selector("div.center-box").find_elements_by_class_name("row")

for body_c in body_content:
    name = driver.find_element_by_xpath("//body/app-root/div[@class='mainContainer']/app-home/div[@class='maplocationblock bs-section']/div[@class='container']/appointment-table/div/div[@class='page-wrapper']/div[@class='register-wrap']/div[@class='padding-0']/div/div[@class='padding-0']/div/div[@class='register-box']/div/div/div/form[@class='ng-invalid ng-dirty ng-touched']/div/div/div[@class='col-padding matlistingblock']/div[@class='center-box']/div[@class='mat-main-field center-main-field']/div/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/div[1]").get_attribute("class")
    # print(name)
    if name == 'slots-box':
        print("Appointment is available.")
    else:
        print("Appointment is not available.")