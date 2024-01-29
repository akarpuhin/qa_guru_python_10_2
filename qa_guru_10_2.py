from selene import browser, be, have

def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_not_available_text():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('1uвыпывпвыпы5!@#$%thtrtr^trhrhrм').press_enter()
    browser.element('[id="result-stats"]')\
        .should(have.text('Результатов: примерно 0'))