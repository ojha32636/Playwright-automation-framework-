class HomePage:
    def __init__(self, page):
        self.page = page
        

    def click_login_link(self):
        self.page.get_by_role("link", name="Sign in").click()

    