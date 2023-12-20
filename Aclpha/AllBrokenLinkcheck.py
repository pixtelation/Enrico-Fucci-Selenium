from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager #---- It is imported for automatic download of driver 
from selenium.webdriver.chrome.service import Service #---- It is imported for automatic download of driver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests


driver_service = Service(executable_path=ChromeDriverManager().install()) #---- Auto installs webdriver, no need to give path.

options = webdriver.ChromeOptions() 
options.add_experimental_option("detach", True) #-------- It is used in order to stop browser being closed automatically.


#--These 3 line is used in order to bypass Cloudflare Human Verification
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")


driver = webdriver.Chrome(service=driver_service, options=options) 
driver.maximize_window()



driver.get("https://google.com/")

# driver.find_element(By.XPATH, "//a[normalize-space()='Log in']").click()
# driver.find_element(By.XPATH, "//input[@id='exampleInputUsername']").send_keys("DHL")
# driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("DHL@123456")
# driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

links = driver.find_elements(By.TAG_NAME,"a")

for link in links:
 ref = link.get_attribute('href') 
 response = requests.get(ref) 
 print((ref),('-'),response.status_code)
 

    
