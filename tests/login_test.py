from pages.login_page import LoginPage

def test_valid_login(page):
    page.goto("https://practicesoftwaretesting.com/", wait_until="domcontentloaded")
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")