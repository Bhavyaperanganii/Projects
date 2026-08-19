from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):

        self.page = page

        self.first_name = page.locator("#firstName")
        self.last_name = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.gender = page.locator("label[for='gender-radio-1']")
        self.mobile = page.locator("#userNumber")
        self.dob = page.locator("#dateOfBirthInput")
        self.subjects = page.locator("#subjectsInput")
        self.hobby = page.locator("label[for='hobbies-checkbox-1']")
        self.address = page.locator("#currentAddress")
        self.state = page.locator("#state")
        self.city = page.locator("#city")
        self.submit_button = page.locator("#submit")


    def enter_first_name(self, value):
        self.first_name.fill(value)


    def enter_last_name(self, value):
        self.last_name.fill(value)


    def enter_email(self, value):
        self.email.fill(value)


    def select_gender(self):
        self.gender.click()


    def enter_mobile(self, value):
        self.mobile.fill(value)


    def select_dob(self):
        self.dob.click()
        self.page.keyboard.press("Enter")


    def enter_subject(self, value):
        self.subjects.fill(value)
        self.page.keyboard.press("Enter")


    def select_hobby(self):
        self.hobby.click()


    def enter_address(self, value):
        self.address.fill(value)


    def select_state_city(self):
        self.state.click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.city.click()
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")


    def click_submit(self):
        self.submit_button.click()