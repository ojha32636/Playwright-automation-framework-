from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.login_data import Valid_Username, Valid_Password
from utils.config import BASE_URL


def test_valid_login(page):
    home_page = HomePage(page)
    HomePage.navigate(home_page, BASE_URL) 
    home_page.click_login_link()
    login_page = LoginPage(page)
    login_page.login(Valid_Username, Valid_Password)
