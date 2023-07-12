import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    browser.quit()