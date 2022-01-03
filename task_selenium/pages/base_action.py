import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://blog.griddynamics.com"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_url(self):
        self.driver.get(self.base_url)

    def check_element_is_presented(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                               message=f"Element {locator} is not presented")

    def check_element_visibility(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                               message=f"Element {locator} is not presented")

    def check_element_enabled(self, locator):
        self.find_element(locator).is_enabled()

    def check_element_is_clickable(self, locator):
        element = self.find_element(locator)
        element.get_property('disabled')

    def move_to_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(2)

    def input_data(self, locator, text):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().send_keys(text).perform()
        assert element is not None, "Data was not inputted"
