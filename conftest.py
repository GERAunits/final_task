import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='None',
                     help="Choose language: ru, en, es, fr ... (etc.)")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser <browser_name> is not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()

# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_addoption(parser):
#     parser.addoption('--language', action='store', default=None,
#                      help="Choose language: es or fr")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     language = request.config.getoption("language")
#     browser = None
#     if language == "es":
#         print("\nstart test language es..")
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})    # ru en
#         browser = webdriver.Chrome(options=options)
#     elif language == "fr":
#         print("\nstart test language fr..")
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})    # ru en
#         browser = webdriver.Chrome(options=options)
#     else:
#         print("\n--language should be es or fr")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
