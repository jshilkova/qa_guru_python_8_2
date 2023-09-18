from selene import have, be
from selene.support.shared import browser


def find_in_google(text):
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()


def expect_search_result_contains(search_result_text):
    browser.element('[id="search"]').should(have.text(search_result_text))


def expect_no_results():
    (browser.element('#result-stats').should(have.text('About 0 results')))