# this is a test file for adding employees

from playwright.sync_api import expect
from pages.add_employee_page import AddEmployee, OpenAddEmployee
from test_data.employee_data import FIRST_NAME, LAST_NAME, USERNAME, PASSWORD


def test_open_add_employee_page(logged_in_page):
    open_add_employee_page = OpenAddEmployee(logged_in_page)
    open_add_employee_page.navigate_to_add_employee_page()
    expect(open_add_employee_page.add_employee_heading).to_be_visible()