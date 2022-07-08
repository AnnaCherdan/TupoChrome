from selenium import webdriver
import pytest


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = 'C:\\Users\\ok_\\AppData\\Local\\chromedriver.exe'
    chrome_options.add_extension('C:\\Program Files (x86)\\Google\\Chrome'
                                 '\\Application\\103.0.5060.114\\Extensions')
    chrome_options.add_argument('--kiosk')
    return chrome_options


@pytest.fixture
def driver_args():
    return ['--log-level=LEVEL']


@pytest.fixture(scope="class")
def driver(request):
    # driver = webdriver.Chrome()
    driver = webdriver.Chrome("C:\\Users\\ok_\\AppData\\Local\\chromedriver.exe")
    # request.cls.driver = driver
