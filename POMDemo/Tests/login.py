from selenium import webdriver
import time
import unittest
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="C:\\Users\\shanmugaml\\PycharmProjects\\Selenium\\Driver\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test01_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # self.driver.find_element_by_id("txtUsername").send_keys("admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    # def test02_login_invalid(self):
    #     driver = self.driver
    #     self.driver.get("https://opensource-demo.orangehrmlive.com")
    #
    #     login = LoginPage(driver)
    #     login.enter_username("Admin1")
    #     login.enter_password("admin1231")
    #     login.click_login()
    #     message = driver.find_element_by_xpath("").text()
    #     self.assertEqual(message, 'Invalid credentials123')
    #     time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\shanmugaml\\PycharmProjects\\Selenium\\Report"))
