class HomePage():

    def __init__(self, driver):  # constarater creted with driver
        self.driver = driver

        self.Welcome_link_id = "welcome"
        self.Logout_link_id = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_id(self.Welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.Logout_link_id).click()


