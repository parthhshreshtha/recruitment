from selenium.webdriver.common.by import By

class InputPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://agrichain.com/qa/input"
        self.input_box = (By.CSS_SELECTOR, "#submitbtn")
        self.submit_btn = (By.CSS_SELECTOR, "#input1")

    def open(self):
        self.driver.get(self.url)

    def enter_input(self, text):
        self.driver.find_element(*self.input_box).send_keys(text)

    def submit(self):
        self.driver.find_element(*self.submit_btn).click()