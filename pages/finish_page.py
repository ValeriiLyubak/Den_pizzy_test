from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    price_total = ''
    # getters


    def get_price_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_total)))
    # actions




    # methods

    def finish(self):
        self.get_current_url()
        self.get_screenshot()

    def take_price_total_end(self):
        price_sum = self.get_price_total()
        price_tot = int(price_sum.text)
        return price_tot











