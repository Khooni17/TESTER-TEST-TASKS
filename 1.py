from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




# 1)
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
# 7) 
min_price = driver.find_element_by_xpath("//input[@id='glpricefrom']")
min_price.send_keys('20000')
# 8)

inpts = driver.find_elements_by_class_name("_3Uz6PcbAtW")
divs = driver.find_elements_by_class_name("LhMupC0dLR")
for i in range(len(inpts)):
	time.sleep(.1)
	if(inpts[i].get_attribute('name') == 'Производитель Apple' or inpts[i].get_attribute('name') == 'Производитель Samsung'):
		divs[i].click()

# 9) теперь кнопки "применить" нет и все применяется автоматически
# 10)


elements = driver.find_elements_by_class_name("n-snippet-cell2")
if(len(elements) == 12):   # у меня изначально по 48 показываются
	pass
#print(num_elements)
# 11)

first_good = elements[0].find_element_by_class_name("n-link_theme_blue").text
print(first_good)

# 12)

driver.find_element_by_xpath("//input[@id='header-search']").send_keys(first_good)
driver.find_element_by_xpath("//span[@class='search2__button']//button[@type='submit']").click()

# 13)

# это если сразу откроется товар
try:
	if( driver.find_element_by_xpath("//h1").text == first_good):
		print(driver.find_element_by_xpath("//h1").text)
		print('ok!')
# но может открыться список доступных модификаций товара, поэтому сравниваю первый товар в списке
except:
	if( driver.find_element_by_class_name('n-snippet-cell2').find_element_by_class_name('n-link_theme_blue').text == first_good):
		print(driver.find_element_by_class_name('n-snippet-cell2').find_element_by_class_name('n-link_theme_blue').text)
		print('ok!')