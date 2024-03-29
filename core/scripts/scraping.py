from selenium import webdriver
from config.driver import DriverSetUp
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle

class ShopeeFlow():
    
  driver = DriverSetUp.set_up()
  
  def login(self, login, password):
    driver = self.driver
    driver.get("https://shopee.com.br/buyer/login?next=https%3A%2F%2Fshopee.com.br%2Fuser%2Fpurchase")

    login_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div[1]/input"))
    )
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div[1]/input"))
    )
    
    form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div/div/div[2]/form"))
    )
    
    login_input.send_keys(login)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    
    time.sleep(1)
    
    # cookies = driver.get_cookies()
    
    # for cookie in cookies:
    #     print(cookie, "\n")
    
    # pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='stardust-popover1']/div"))).is_displayed()
    
  def check_order_track_status(self, order_id):

    order_id_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='main']/div/div[2]/div/div[2]/div/div[4]/input")))

    order_id_input.send_keys(order_id)
    order_id_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "shopee-image__wrapper"))
    ).click()

    track_status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "w5KHDc"))).screenshot("/core/screenshots/status.png")
    