from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.username_input = self.page.get_by_placeholder("Your email")
        self.password_input = self.page.get_by_placeholder("Your password")
        self.login_button = self.page.get_by_role("button", name="Login")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        