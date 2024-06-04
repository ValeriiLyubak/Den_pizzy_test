import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base
from pages.landing_page import driver


class Main_page(Base):
    actions = ActionChains(driver)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    select_peperoni = '//*[@id="category_id-278"]/div/article[2]/div[3]/div'
    confirm = '//*[@id="js-main"]/div/div[3]/article/div[2]/div/div[1]/div/button'
    price_peperoni = ''
    price_denpizzy = ''
    select_denpizzy = ''
    cart = ''
    link_akcii = ''

    # getters



    def get_select_peperoni(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_peperoni)))

    def get_select_denpizzy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_denpizzy)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_link_akcii(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_akcii)))

    def get_price_peperoni(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_peperoni)))

    def get_price_denpizzy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_denpizzy)))

    def get_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm)))


    # actions

    def move_to_pizza(self):
        ActionChains(self.driver).move_to_element(self.get_select_peperoni()).perform()


    def click_select_select_peperoni(self):
        self.get_select_peperoni().click()
        print('click select_peperoni')

    def click_select_select_denpizzy(self):
        self.get_select_denpizzy().click()
        print('click select_denpizzy')

    def click_cart(self):
        self.get_cart().click()
        print('click cart')

    def click_link_akcii(self):
        self.get_link_akcii().click()
        print('click link_akcii')

    def click_confirm(self):
        self.get_confirm().click()
        print('click confirm')


    def move_to_confirm(self):
        ActionChains(self.driver).move_to_element(self.get_confirm()).perform()



    def select_2_pizzas(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.move_to_pizza()
        self.click_select_select_peperoni()
        time.sleep(1)
        self.move_to_confirm()
        time.sleep(1)
        self.click_confirm()
        self.click_select_select_denpizzy()
        time.sleep(1)
        self.move_to_confirm()
        self.click_confirm()
        self.click_cart()



    def select_link_akcii(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_link_akcii()
        self.assert_url('https://daypizza.ru/voronezh/promotions')
        print('assertion success')

    def take_price_peperoni(self):
        price_sum = self.get_price_peperoni()
        price_pep = int(price_sum.text)
        return price_pep

    def take_price_denpizzy(self):
        price_sum = self.get_price_denpizzy()
        price_dp = int(price_sum.text)
        return price_dp





