from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        
    def click_login_link(self):
        self.page.get_by_role("link", name="Sign in").click()

   