from selenium import webdriver

def browser():
    driver_path = "./drivers/chromedriver.exe"
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    return driver