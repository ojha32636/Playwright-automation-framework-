from pages.home_page import HomePage
from playwright.sync_api import expect
from utils.config import BASE_URL, LOGIN_URL

# verifying that it has title and the title is correct
def test_home_page_title(page):
    home_page = HomePage(page)

    HomePage.navigate(home_page, BASE_URL)

    expect(page).to_have_title(
        "Practice Software Testing - Toolshop - v5.0"
    )

# # verifying that the login link is present and clickable
def test_click_login_link(page):
    home_page = HomePage(page)
    HomePage.navigate(home_page, BASE_URL) 
    click_login_link = HomePage(page)
    click_login_link.click_login_link()
    expect(page).to_have_url(LOGIN_URL)
   