import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: es, fr, en")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption("language")
    browser = None

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
    
    if browser_name == 'chrome':
        browser = webdriver.Chrome(options=options)
        print("\nstart Chrome browser for test..")
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(options=options_firefox)
        print("\nstart Firefox browser for test..")
    else:
        raise pytest.UsageError('Browser"s name should be chrome or firefox')
        
    yield browser
    print("\nquit browser..")
    browser.quit()