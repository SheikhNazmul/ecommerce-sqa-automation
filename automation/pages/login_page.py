from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "email")
    password = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self, base_url):
        self.driver.get(f"{base_url}/login")

    def login(self, email_value, password_value):
        self.driver.find_element(*self.email).send_keys(email_value)
        self.driver.find_element(*self.password).send_keys(password_value)
        self.driver.find_element(*self.login_button).click()
