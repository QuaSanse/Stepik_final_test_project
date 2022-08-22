import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options as firefox_options


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help="Choose languages: ru, en, ... (etc.)")


@pytest.fixture
def get_chrome_options(request) -> chrome_options:
    options = chrome_options()
    options.add_argument('crome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1200,1080')
    user_language = request.config.getoption("language")  # язык пользователя
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    return options


@pytest.fixture
def get_firefox_options(request):
    options = firefox_options()
    # options.add_argument('firefox')
    # options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1200,1080')
    # options = webdriver.FirefoxProfile()
    user_language = request.config.getoption("language")  # язык пользователя
    options.set_preference('prefs', {'intl.accept_languages': user_language})
    return options


@pytest.fixture
def get_webdriver(request, get_chrome_options, get_firefox_options) -> webdriver:
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        options = get_chrome_options
        print("\nstart Chrome browser for test...")
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser_name == "firefox":
        firefox_options = get_firefox_options
        print("\nstart Firefox browser for test...")
        driver = webdriver.Firefox(firefox_profile=firefox_options)
        return driver
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


@pytest.fixture(scope='function') 
def driver(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    yield driver

    driver.close()
    print("\nquit browser...")
    driver.quit()
