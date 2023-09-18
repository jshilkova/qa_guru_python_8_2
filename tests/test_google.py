import pytest
from modules.google_search import *


@pytest.fixture(autouse=True)
def open_google():
    browser.open('https://google.com')


def test_google_should_find_selene():
    find_in_google('yashaka/selene')
    expect_search_result_contains('Selene - User-oriented Web UI browser tests in Python')


def test_google_should_not_find_nonsense():
    find_in_google('awvhtsfjsssqqqqq')
    expect_no_results()
