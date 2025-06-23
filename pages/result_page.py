from selenium.webdriver.common.by import By

class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.output = (By.CSS_SELECTOR, ".output")

    def get_result_text(self):
        return self.driver.find_element(*self.output).text