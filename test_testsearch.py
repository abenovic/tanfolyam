# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


class TestTestsearch():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testsearch(self):
    self.driver.get("https://www.python.org/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "id-search-field").click()
    self.driver.find_element(By.ID, "id-search-field").send_keys("pip 008")
    self.driver.find_element(By.ID, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".list-recent-events > p").text == "No results found."
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
  
