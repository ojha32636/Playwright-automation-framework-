from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_valid_login(page):
    page.goto("https://practicesoftwaretesting.com/", wait_until="domcontentloaded")
    home_page = HomePage(page)
    home_page.click_login_link()
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")