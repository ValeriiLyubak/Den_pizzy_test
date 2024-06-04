import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base
from pages.landing_page import driver


class Client_information_page(Base):
    actions = ActionChains(driver)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    delivery = '//*[@id="pickup_tab"]'
    comment = '//*[@id="order_comment"]'
    continue_button = ''
    price_total = ''

    # getters

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_price_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_total)))

    # actions

    def click_delivery(self):
        self.get_delivery().click()
        print('click delivery')

    def input_comment(self, comment):
        comment_field = self.get_comment()
        comment_field.click()
        time.sleep(1)
        comment_field.send_keys(comment)
        print('input comment')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('click continue_button')

    def move_to_continue_button(self):
        ActionChains(self.driver).move_to_element(self.get_continue_button()).perform()

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.40);")

    # methods

    def input_information(self):
        self.get_current_url()
        self.driver.maximize_window()
        self.click_delivery()
        self.scroll_page_down()
        self.move_to_continue_button()
        self.input_comment('пожалуйста извините, удалите заказ, я проверял аккаунт')
        self.click_continue_button()

    def print_price_total(self):
        price_checkout = self.get_price_total()
        price_dp = price_checkout.text
        print(price_dp)







