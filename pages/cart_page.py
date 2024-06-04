import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base
from pages.landing_page import driver


class Cart_page(Base):
    actions = ActionChains(driver)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    checkout_button = ''


    # getters


    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('click checkout_button')


    def move_checkout_button(self):
        ActionChains(self.driver).move_to_element(self.get_checkout_button()).perform()

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.50);")


    # methods

    def product_confirmation(self):
        self.get_current_url()
        time.sleep(2)
        self.scroll_page_down()
        self.move_checkout_button()
        self.click_checkout_button()










