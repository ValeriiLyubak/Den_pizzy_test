from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)



from base.base_class import Base


class Landing_page(Base):
    url = 'https://daypizza.ru/voronezh/'
    confirm = "//*[@data-testid='cityConfirmation']"

    def get_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm)))

    def click_confirm(self):
        self.get_confirm().click()
        print('click confirm')

    def landing_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_confirm()
        print('landing succesfuly complete')











