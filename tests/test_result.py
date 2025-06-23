import time
from utils.browser import browser
from pages.input_page import InputPage
from pages.result_page import ResultPage

def test_longest_unique_substring():
    driver = browser()

    try:
        input_page = InputPage(driver)
        result_page = ResultPage(driver)
        test_input = "abcabcbb"
        expected_output = "3"

        input_page.open()
        input_page.enter_input(test_input)
        input_page.submit()

        time.sleep(2)

        #Comparing results
        output = result_page.get_result_text()
        assert output == expected_output, f"Expected {expected_output}, Actual {output}"

    finally:
        driver.quit()