import unittest

from Config.config import TestData
from selenium import webdriver

from Pages.Home_Page import Home_Page
from Pages.Login import Login


class LOGOUT(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=TestData.Chrome_Executable_Path)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.Base_Url)

    def test_logout(self):
        login = Login(self.driver)
        home = Home_Page(self.driver)
        login.login_into_app()
        home.logout_functionality()

