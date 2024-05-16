from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=chrome_options)



from base.base_class import Base


class Landing_page(Base):
    url = 'https://daypizza.ru/voronezh/'


    def landing_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        print('landing succesfuly complete')











