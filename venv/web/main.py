from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('http://flash-admin.enilu.cn/#/login?redirect=%2Fdashboard')
# time.sleep(5) 固定
driver.implicitly_wait(10)  # 智能等待
selenium.webdriver.remote.webelement.WebElement

driver.find_element(By.NAME,'username')


print(type(driver.find_element_by_name('username')))
driver.find_element_by_name('password')

# 元素：selenium针对所有元素进行封装，显示的属性和方法是相同的
# html css js w3c输入框，按钮，单选框，下拉框，超链接，复选框，图片......  WebElement
# 入门级，菜鸟教程，高手，设计模式，python hook

#
# driver.find_element_by_name('username')
# driver.find_element(By.NAME, 'username')

# elements = driver.find_elements_by_tag_name('input')
# elements = driver.find_elements(By.TAG_NAME, 'input')
# submit = driver.find_element_by_xpath('//*[@id="app"]/div/form/button')


# Page--》WebElement
# 数据类型：字典、元组、列表、集合
