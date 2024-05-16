import time

from selenium import webdriver

from pages.landing_page import Landing_page
from pages.main_page import Main_page


def test_link_about():
    driver = webdriver.Chrome()

    print('start page akcii test')

    lp = Landing_page(driver)
    lp.landing_page()

    mp = Main_page(driver)
    mp.select_link_akcii()

    print('finish page akcii test')
    time.sleep(2)
    driver.quit()



