import pytest
from selenium import webdriver
from Library.config import Config

from selenium.webdriver.firefox.options import Options

#Cross Browsing
firefox_Driver_path = r"C:\Users\Mohite's\Downloads\chromedriver_win32\geckodriver.exe"
@pytest.fixture(params=["Chrome","Edge","Firefox"])
def _driver(request):

    if request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_Driver_path)


    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_Driver_Path)

    elif request.param == "Firefox":
        options = Options()
        options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=firefox_Driver_path,options=options)








    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    print(driver.title)

    driver.close()
