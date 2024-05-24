import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    """method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        name_screenshot = now_date + '.png'
        self.driver.save_screenshot('screen/'+name_screenshot)

    """metod assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('assert url success')