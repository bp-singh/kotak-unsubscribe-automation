from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path= "C:\\chromedriver.exe")
url =  "https://docs.google.com/forms/d/e/1FAIpQLSdw9iK20-j3r6a00cgM2Uy_ZWVQHcz3Cz3OxeeMuKzkOBKQ4Q/viewform"

driver.get(url)
number = int(9999998319)
driver.maximize_window()
i = 1
while True:
    try:
        no = (number-i)
        print (no)
        time.sleep(1)
        element = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        element.send_keys("Kotak 811 - Unsubscribe Form")
        time.sleep(1)
        element = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        element.send_keys(no)
        time.sleep(1)
        element = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div/span/span")
        element.click()
        time.sleep(1)
        element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        element.click()
        time.sleep(1)
        i = i+1
    except:
        pass

print("all numbers subscribe message has been sent")
driver.close()
    

    
