from selenium import  webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

sleep(2)

#第一种方法
#driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()

#第二种方法
ele_string = driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
if (ele_string == "Selenium - Web Browser Automation"):
    print('测试成功，结果与预期匹配')

driver.quit()


sleep(2)
driver.quit()


