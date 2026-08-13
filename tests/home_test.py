from pages.home_page import HomePage
from playwright.sync_api import expect

# verifying that it has title and the title is correct
def test_home_page_title(page):
    page.goto("https://practicesoftwaretesting.com/", wait_until="domcontentloaded")
    home_page = HomePage(page)

    expect(page).to_have_title(
        "Practice Software Testing - Toolshop - v5.0"
    )

# verifying that the login link is present and clickable
def test_click_login_link(page):
    page.goto("https://practicesoftwaretesting.com/", wait_until="domcontentloaded")
    home_page = HomePage(page)
    home_page.click_login_link()
    expect(page).to_have_url(
        "https://practicesoftwaretesting.com/auth/login"
    )