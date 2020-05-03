from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time # импортирован для удобной проверки п.2 по плану

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
selector = '#add_to_basket_form>.btn-add-to-basket'

def test_check_addbuttons(browser):
	browser.get(link)
	#time.sleep(30) #Раскомментировать для проверки с fr
	addbuttons = WebDriverWait(browser, 5).until(
	EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
	# Проверяем наличие кнопка на странице и можем её нажать
	assert addbuttons, "Кнопку добавления в корзину укарали :)"