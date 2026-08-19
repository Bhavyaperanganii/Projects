from pages.register_page import RegisterPage


def test_register_user(page):

    page.goto("https://demoqa.com/automation-practice-form")

    register = RegisterPage(page)

    register.enter_first_name("Bhavya")

    register.enter_last_name("Perangani")

    register.enter_email("bhavya123@gmail.com")

    register.select_gender()

    register.enter_mobile("9876543210")

    register.select_dob()

    register.enter_subject("Maths")

    register.select_hobby()

    register.enter_address("India")

    register.select_state_city()

    register.click_submit()


    # verify registration popup
    assert page.locator(".modal-title").is_visible()