# this page will contain the locators and methods for the home page of the application.


from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage

def test_dashboard_page_elements(logged_in_page):
    # Verify the title is visible
    dashboard_page = DashboardPage(logged_in_page)

    expect(dashboard_page.dashboard_heading).to_be_visible()
