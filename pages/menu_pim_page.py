# This page is used to add a new employee to the system. It contains a form that collects the employee's details and submits them to the backend for processing.

from pages.dashboard_page import DashboardPage


# open the add employee page and fill in the form with the employee's details, then submit the form to add the employee to the system.
class PimPage(DashboardPage):
    def __init__(self, page):
        super().__init__(page)
       
        self.PIM_menu = self.page.locator("a[href='/web/index.php/pim/viewPimModule']"
                                          )
        self.add_employee_heading = self.page.locator(
            "//a[normalize-space()='Add Employee']"
            )
    
    def open_PIM_menu(self):
        self.PIM_menu.click()

    def click_add_employee_heading(self):
        self.add_employee_heading.click()    

class AddEmployee(PimPage):
 def __init__(self, page):
        super().__init__(page)
        self.navigate_to_add_employee_page()
        self.add_employee_button = self.page.locator("button[title='Add Employee']")
        self.first_name_input = self.page.locator("input[name='firstName']")
        self.last_name_input = self.page.locator("input[name='lastName']")
        self.username_input = self.page.locator("input[name='username']")
        self.password_input = self.page.locator("input[name='password']")
        self.save_button = self.page.locator("button[type='submit']")