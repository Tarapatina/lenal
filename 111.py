from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://www.liebherr.lenal.company")
button = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/a').click()

#driver.quit()