class LoginPage():

    def __init__(self, driver):     #constarater creted with driver
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.passsword_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"
        self.invalidUsername_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.passsword_textbox_id).clear()
        self.driver.find_element_by_id(self.passsword_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_invalid_user_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidUsername_xpath).text()
        return
