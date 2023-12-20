from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service #---- It is imported for automatic download of driver 
from selenium.webdriver.chrome.options import Options  #------ Options are imported to use it to stop automaticallly closing driver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver_service = Service(executable_path=ChromeDriverManager().install()) #---- Auto installs webdriver, no need to give path.

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True) #-------- It is used in order to stop browser being closed automatically.

driver = webdriver.Chrome(service=driver_service, options=options) 
driver.maximize_window()

driver.implicitly_wait(30)

driver.get("https://walkfitplatinum.com/")
driver.find_element(By.LINK_TEXT, "Order Now").click()
driver.find_element(By.XPATH, "(//span[@class='variable-item-span variable-item-span-button'])[2]").click()
driver.find_element(By.XPATH, "(//span[@class='variable-item-span variable-item-span-button'])[4]").click()
driver.find_element(By.XPATH, "//button[@class='single_add_to_cart_button button alt']").click()
driver.find_element(By.XPATH, "//a[@class='button checkout wc-forward']").click()
driver.find_element(By.XPATH, "//div[@data-button-text='true']").click()
driver.find_element(By.LINK_TEXT, "No Thank You").click()


