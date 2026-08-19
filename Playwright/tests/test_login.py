from pages.login_page import LoginPage


def test_login_success(page):

    page.goto("https://www.saucedemo.com/")

    login = LoginPage(page)

    login.enter_username("standard_user")

    login.enter_password("secret_sauce")
    login.click_login()
    
    assert page.url == "https://www.saucedemo.com/inventory.html"