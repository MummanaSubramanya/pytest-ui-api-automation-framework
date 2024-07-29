import configparser
import pytest
import datetime

from utils.config_parser import ReadProperties
from utils.entity_creator import create_new_user_data

from apis.app import Application

from selenium import webdriver


# reads parameters from pytest command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")
    parser.addoption("--env", action="store", default="DEV", help="browser that the automation will run in")
  
  
@pytest.fixture(scope='session')
def environment_config(pytestconfig):
    # Get the environment name and read config file
    env = pytestconfig.getoption("env")
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # Return the section of the configuration based on the environment
    if env in config:
        return config[env]
    else:
        raise ValueError(f"Environment '{env}' not found in the configuration file")

 
@pytest.fixture(scope="session")
def app(environment_config):
    return Application(environment_config)


@pytest.fixture(scope='function')
def create_user(app: Application):
    user = create_new_user_data()
    return app.user_operations.create_new_user_successfully(user)


@pytest.fixture(scope='function')
def create_driver(environment_config, request):
    """Note: The request object in pytest fixtures provides access to information about the executing test function or class."""
    browser = request.config.option.browser
    base_url = environment_config['base_url']
    
    if browser == "safari":
        options = webdriver.SafariOptions()
        driver = webdriver.Safari(options=options)
    elif browser == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        driver = webdriver.Chrome(options=opts)
    elif browser == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(options=opts)
    else:
        raise ValueError(f'{browser} is not availble.')
    
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    item = request.node
    if item.rep_call.failed:
        screenshot_name = 'screenshot on failure: %s' % datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
    driver.quit()


@pytest.fixture(params=["chrome", "edge"], scope="function")
def multi_driver(environment_config, request: pytest.FixtureRequest):
    base_url = environment_config['base_url']
    if request.param == "edge":
        opts = webdriver.EdgeOptions()
        opts.add_argument("--headless")
        driver = webdriver.Edge(options=opts)
    elif request.param == "chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        driver = webdriver.Chrome(options=opts)
    elif request.param == "firefox":
        opts = webdriver.FirefoxOptions()
        opts.add_argument("--headless")
        driver = webdriver.Firefox(options=opts)
    else:
        raise ValueError(f'{request.param} is not availble.')
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.quit()   

 
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)        
    