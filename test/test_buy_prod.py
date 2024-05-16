import time

from selenium import webdriver


from pages.cart_page import Cart_page
from pages.client_info_page import Client_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.landing_page import Landing_page


def test_select_pizzas():
    driver = webdriver.Chrome()

    print('start pizza product route test')

    lp = Landing_page(driver)
    lp.landing_page()

    mp = Main_page(driver)
    mp.select_2_pizzas()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    f = Finish_page(driver)
    f.finish()

    print('finish pizza product route test')
    time.sleep(2)
    driver.quit()


