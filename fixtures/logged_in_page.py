# this page will be used to remain logged in for after login tests.

import pytest

from pages.login_page import LoginPage
from test_data.login_data import VALID_PASSWORD, VALID_USERNAME
from utils.config import BASE_URL


@pytest.fixture
def logged_in_page(page):

    login_page = LoginPage(page)

    login_page.navigate(BASE_URL)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    return page