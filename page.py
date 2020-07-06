from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def get_page_title(self):
        return self.driver.title


class MainPage(Page):
    URL = "https://www.seleniumeasy.com/test/"
    __INPUT_FORMS = "//*[@id='treemenu']//a[text()='Input Forms']"
    __SIMPLE_FORM = "//*[@id='treemenu']//a[text()='Simple Form Demo']"

    def load(self):
        self.driver.get(self.URL)

    def navigate_to_simple_forms(self):
        self.driver.find_element_by_xpath(self.__INPUT_FORMS).click()
        self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.__SIMPLE_FORM))).click()


class FormPage(Page):
    __SINGLE_INPUT = "//*[@id='user-message']"
    __SHOW_MESSAGE_BUTTON = "//*[@id='get-input']/button"
    __DISPLAY_MESSAGE = "//*[@id='display']"
    __MULTIPLE_INPUT_A = "//*[@id='sum1']"
    __MULTIPLE_INPUT_B = "//*[@id='sum2']"
    __GET_TOTAL_BUTTON = "//*[@id='gettotal']/button"
    __DISPLAY_SUM = "//*[@id='displayvalue']"

    def single_input(self, text):
        self.driver.find_element_by_xpath(self.__SINGLE_INPUT).send_keys(text)
        self.driver.find_element_by_xpath(self.__SHOW_MESSAGE_BUTTON).click()
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.__DISPLAY_MESSAGE))).text

    def multiple_input(self, input_a, input_b):
        self.driver.find_element_by_xpath(
            self.__MULTIPLE_INPUT_A).send_keys(input_a)
        self.driver.find_element_by_xpath(
            self.__MULTIPLE_INPUT_B).send_keys(input_b)
        self.driver.find_element_by_xpath(self.__GET_TOTAL_BUTTON).click()
        return self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.__DISPLAY_SUM))).text
