import time

from selenium import webdriver

from pages.cart_page import Cart_page
from pages.client_info_page import Client_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.landing_page import Landing_page


def test_select_pizzas():
    driver = webdriver.Chrome()

    print('start asser pizza test')

    lp = Landing_page(driver)
    lp.landing_page()

# """сравниваю сумму двух пицц на стартовой странице и сумму заказа на чекауте"""

    mp = Main_page(driver)
    price_pep = mp.take_price_peperoni()
    price_dp = mp.take_price_denpizzy()
    sum_pizzas = int(price_pep) + int(price_dp)
    print(sum_pizzas)

    mp = Main_page(driver)
    mp.select_2_pizzas()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    fp = Finish_page(driver)
    total_end_price = fp.take_price_total_end()
    print(total_end_price)

    assert sum_pizzas == total_end_price

    print('сумма пицц равна')

    print('finish asser pizza test')
    time.sleep(2)
    driver.quit()


