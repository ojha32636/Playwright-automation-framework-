# this is a test file for adding employees

from playwright.sync_api import expect
from pages.menu_pim_page import AddEmployee, PimPage
from test_data.employee_data import FIRST_NAME, LAST_NAME, USERNAME, PASSWORD


def test_navigate_to_pim_menu(logged_in_page):
    open_pim_page = PimPage(logged_in_page)
    open_pim_page.open_PIM_menu()
    expect(open_pim_page.add_employee_heading).to_be_visible()

def test_navigate_to_add_employee_page(logged_in_page):    
    open_pim_page = PimPage(logged_in_page)
    open_pim_page.open_PIM_menu()
    open_pim_page.click_add_employee_heading()
    expect(open_pim_page.add_employee_heading).to_be_visible()