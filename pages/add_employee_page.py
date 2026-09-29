# This page is used to add a new employee to the system. It contains a form that collects the employee's details and submits them to the backend for processing.

from pages.dashboard_page import DashboardPage
from test_data.employee_data import FIRST_NAME, LAST_NAME, USERNAME, PASSWORD

# open the add employee page and fill in the form with the employee's details, then submit the form to add the employee to the system.
class OpenAddEmployee(DashboardPage):
    def __init__(self, page):
        super().__init__(page)
       
        self.PIM_menu = self.page.locator("a[href='/web/index.php/pim/viewPimModule']"
                                          )

      
        self.add_employee_heading = self.page.locator(
            "//a[normalize-space()='Add Employee']"
            )
    
    def navigate_to_add_employee_page(self):
        self.PIM_menu.click()
        self.add_employee_heading.click()    

class AddEmployee(DashboardPage):
 def __init__(self, page):
        super().__init__(page)
        self.PIM_menu = self.page.locator("a[href='/web/index.php/pim/viewPimModule']")
        self.add_employee_heading = self.page.locator(
            "h6.oxd-text.oxd-text--h6.oxd-topbar-header-breadcrumb-module"
            )
        self.add_employee_button = self.page.locator("button[title='Add Employee']")
        self.first_name_input = self.page.locator("input[name='firstName']")
        self.last_name_input = self.page.locator("input[name='lastName']")
        self.username_input = self.page.locator("input[name='username']")
        self.password_input = self.page.locator("input[name='password']")
        self.save_button = self.page.locator("button[type='submit']")