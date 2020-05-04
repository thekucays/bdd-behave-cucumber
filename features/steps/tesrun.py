# from behave import given, when, then
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from xpaths.xpath_web_homepage import *
from xpaths.web_register.xpath_web_register import *

@given('buka aplikasi')
def step_impl(self):
	print "buka aplikasi nya"
	self.driver = webdriver.Chrome()
	self.driver.get("https://staging.cicil.dev")
	# driver.maximize_window()
    # raise NotImplementedError('STEP: Given buka aplikasi')


@when('masuk ke halaman login dan input data')
def step_impl(self):
	time.sleep(3)
	self.driver.maximize_window()
	self.driver.find_element(By.XPATH, daftar_button_homepage).click()
	time.sleep(10)
	self.driver.find_element(By.XPATH, email_input_register).send_keys('testing@cicil.co.id')
	time.sleep(10)


@then('tes printout then')
def step_impl(self):
	print "tes printout then"
    # raise NotImplementedError('STEP: Then tes printout then')
