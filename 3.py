from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.maximize_window()
# 2)
driver.get('http://yandex.ru')
# 3)
market = driver.find_element_by_xpath("//a[@class='home-link home-link_blue_yes home-tabs__link home-tabs__search'][contains(text(),'Маркет')]")
market.click()

# 4)
time.sleep(10)

electronic = driver.find_element_by_class_name("topmenu__link")
electronic.click()
# 5)
time.sleep(10)
mobiles = driver.find_element_by_xpath("//a[@class='_2qvOOvezty _2x2zBaVN-3 _9qbcyI_fyS'][contains(text(),'Мобильные телефоны')]")
mobiles.click()

# 6)

driver.find_element_by_xpath("//a[contains(text(),'по цене')]").click()
time.sleep(3)
# 7)

elems = driver.find_elements_by_class_name('n-snippet-cell2')

prices = [int(elem.find_element_by_class_name('price').text.split(' ₽')[0]) for elem in elems]
print(prices)
if sorted(prices) == prices:
	print('ok')