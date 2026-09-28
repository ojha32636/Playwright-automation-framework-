from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.login_data import VALID_PASSWORD, VALID_USERNAME, INVALID_PASSWORD
from utils.config import BASE_URL, ACCOUNT_URL, LOGIN_URL
from playwright.sync_api import expect



def test_valid_login(page):
    home_page = HomePage(page)
    home_page.navigate(BASE_URL) 
    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    expect(page).to_have_url(
        ACCOUNT_URL
    )     

def test_invalid_login(page):
    home_page = HomePage(page)
    home_page.navigate(BASE_URL) 
    login_page = LoginPage(page)
    login_page.login(VALID_USERNAME,INVALID_PASSWORD)
    
    expect(page).to_have_url(
        LOGIN_URL
        
    )
    