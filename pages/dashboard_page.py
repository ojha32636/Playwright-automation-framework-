# this page will cover dashboard page elements and actions
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.dashboard_heading = self.page.locator(
            "h6.oxd-topbar-header-breadcrumb-module"
            )