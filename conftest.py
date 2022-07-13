from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture
# def chrome_options(chrome_options):
#     my_options = chrome_options
#     driver = webdriver.Chrome(chrome_options=my_options)
#     chrome_options.binary_location = '/usr/local/bin/chromedriver'
#     # chrome_options.add_extension('/opt/google/chrome/default_appsExtensions')
#     chrome_options.add_argument('--kiosk')
#     return chrome_options


@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL']


@pytest.fixture
def veb_driver(request):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    # request.cls.driver = driver
    return driver
