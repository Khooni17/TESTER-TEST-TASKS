from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.maximize_window()



#1

driver.get('https://anketa.alfabank.ru/alfaform-refpil/step1')
time.sleep(1)
# фамилия
driver.find_element_by_xpath("//input[@name='lastName']").send_keys('иванов')
# имя
driver.find_element_by_xpath("//input[@name='firstName']").send_keys('иван')
#отчество
driver.find_element_by_xpath("//input[@name='middleName']").send_keys('иванович')
# мобила
driver.find_element_by_xpath("//input[@name='mobilePhone']").send_keys('9001234567')
# почта
driver.find_element_by_xpath("//input[@name='email']").send_keys('test@mail.ru')
# регион
driver.find_element_by_xpath("//input[@name='workRegionCode']").send_keys('Москва')
time.sleep(.1)
driver.find_element_by_xpath("//span[contains(text(),'Москва')]").click()


driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)




# 2

#серия 
driver.find_element_by_xpath("//input[@placeholder='Серия']").send_keys('1234')
#Номер
driver.find_element_by_xpath("//input[@placeholder='Номер']").send_keys('567891')
#дата
driver.find_element_by_xpath("//input[@placeholder='ДД.ММ.ГГГГ']").send_keys('11.11.2010')
# Код подразделения
driver.find_element_by_xpath("//input[@name='passportOfficeCode']").send_keys('123-456')
# Кем выдан
who = driver.find_element_by_xpath("//textarea[@name='passportOffice']")
who.send_keys(Keys.TAB)
who.clear()
who.send_keys("земля")
# дата рождения

driver.find_elements_by_xpath("//input[@placeholder='ДД.ММ.ГГГГ']")[1].send_keys('11.11.1980', Keys.ENTER)
# место рождения
driver.find_element_by_xpath("//input[@name='passportBirthPlace']").send_keys('земля')
# регион регистрации
driver.find_element_by_xpath("//input[@name='registrationRegionCode']").send_keys('Москва')
time.sleep(.1)
driver.find_element_by_xpath("//span[contains(text(),'Москва')]").click()
# название организации
driver.find_element_by_xpath("//input[@name='workCompanyName']").send_keys('apple')
# ИНН организации
driver.find_element_by_xpath("//input[@name='workInn']").send_keys('250907607034') # первое, что нашел в интернете, случайные числа он не пускает
# зп
driver.find_element_by_xpath("//input[@name='income']").send_keys('25000')

driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)



# 3

driver.find_element_by_xpath("//input[@placeholder='ДД.ММ.ГГГГ']").send_keys('20.10.2000')

driver.find_element_by_xpath("//input[@name='workPost']").send_keys('вфы')

driver.find_element_by_xpath("//input[@name='workPhone']").send_keys('9823322523')    

driver.find_elements_by_class_name("select-button_theme_alfa-on-white")[0].click()
time.sleep(1)
driver.find_elements_by_class_name("menu-item_theme_alfa-on-white")[2].click()

driver.find_elements_by_class_name("select-button_theme_alfa-on-white")[1].click()
time.sleep(1)
driver.find_elements_by_class_name("menu-item_theme_alfa-on-white")[8].click()


driver.find_elements_by_class_name("select-button_theme_alfa-on-white")[2].click()
time.sleep(1)
driver.find_elements_by_class_name("menu-item_theme_alfa-on-white")[15].click()


driver.find_element_by_xpath("//input[@name='contactLastName']").send_keys('cads')
driver.find_element_by_xpath("//input[@name='contactFirstName']").send_keys('saf')
driver.find_element_by_xpath("//input[@name='contactMiddleName']").send_keys('asf')
driver.find_element_by_xpath("//input[@name='contactMobilePhone']").send_keys('9999222883') 	
 
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

  

driver.find_element_by_class_name('tag-button_togglable_check').click()

driver.find_elements_by_class_name('tag-button_togglable_check')[3].click()
















