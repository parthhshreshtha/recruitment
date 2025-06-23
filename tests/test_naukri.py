from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# === Step 1: Set up ChromeDriver correctly ===
driver_path = "D:/chromedriver.exe"  # Path to manually downloaded driver
service = Service(driver_path)

options = webdriver.ChromeOptions()
options.add_argument(r'user-data-dir=C:\Seleniumchromeprofile')
options.add_argument("--profile-directory=Default")  # or "Profile 1", etc.
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.naukri.com")
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "#login_Layer").click()
# time.sleep(2)
# email = driver.find_element(By.CSS_SELECTOR, ".drawer-wrapper .form-row:nth-child(2) input")
# email.click()
# email.send_keys("parthshreshtha.cpp@gmail.com")

# passw = driver.find_element(By.CSS_SELECTOR, ".drawer-wrapper .form-row:nth-child(3) input")
# passw.click()
# passw.send_keys("Naukri@2770")

# login = driver.find_element(By.CSS_SELECTOR, ".btn-primary.loginButton")
# login.click()
bars = driver.find_element(By.CSS_SELECTOR, ".profile-perf-content a")
bars.click()
# view = driver.find_element(By.CSS_SELECTOR, ".nI-gNb-de__perf-card:nth-child(1) .nI-gNb-de__perf-card-view")
# view.click()
share = driver.find_element(By.CSS_SELECTOR, ".spc__header a")
share.click()
time.sleep(3)
limit = len(driver.find_elements(By.CLASS_NAME, "tlc__tuple"))
print(limit)
while (limit != 0):
    for i in range(1,limit+1):    
        driver.find_element(By.CSS_SELECTOR, f".tlc__tuple:nth-child({i}) button").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)