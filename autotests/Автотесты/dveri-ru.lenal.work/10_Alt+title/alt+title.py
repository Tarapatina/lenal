from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
with open('url_file.txt', 'r') as url_list:
    for el in url_list.readlines():
        response = driver.get(el.replace('\n', ''))
        buy = driver.find_element_by_xpath('//div[@class=" goods-info-right hidden-sm hidden-xs"]//button').click()

    try:
        offer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Оформить заказ")]')))
        offer.click()
        t = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//h4/following-sibling::p[1]/span'))).text
        print(t)
    finally:
        driver.close()




