from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")


    def enter_username(self, username):
        self.username_input.fill(username)


    def enter_password(self, password):
        self.password_input.fill(password)


    def click_login(self):
        self.login_button.click()