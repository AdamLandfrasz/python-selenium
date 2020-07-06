from page import MainPage, FormPage
from selenium.webdriver import Chrome
import unittest


class TestSeleniumEasy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome()
        cls.main_page = MainPage(cls.driver)
        cls.form_page = FormPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_main_smoke(self):
        self.main_page.load()
        assert "Best Demo" in self.main_page.get_page_title()

    def test_form_smoke(self):
        self.main_page.load()
        self.main_page.navigate_to_simple_forms()
        assert "Simple Form" in self.form_page.get_page_title()

    def test_single_input_happy(self):
        self.main_page.load()
        self.main_page.navigate_to_simple_forms()
        assert "test text" == self.form_page.single_input("test text")

    def test_multiple_input_happy(self):
        self.main_page.load()
        self.main_page.navigate_to_simple_forms()
        assert "5" == self.form_page.multiple_input("2", "3")
