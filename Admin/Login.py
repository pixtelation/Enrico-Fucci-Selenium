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


driver.get("https://dev.groundmetrx.com/")
driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
driver.find_element(By.XPATH, "//input[@id='exampleInputUsername']").send_keys("DHL")
driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("DHL@123456")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

driver.find_element(By.XPATH, "//a[normalize-space()='Administration']").click()
driver.find_element(By.XPATH, "//a[normalize-space()='Employees']").click()
