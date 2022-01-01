import allure

from task_selenium.pages.base_action import BaseAction
from task_selenium.pages.locators import GDSeacrhLocators


class MainPage(BaseAction):

    @allure.step("Open on About page")
    def click_about(self):
        self.find_element(GDSeacrhLocators.ABOUT).click()

    @allure.step("Check Filter available and visible")
    def check_filter_presented_and_available(self):
        self.check_element_is_presented(GDSeacrhLocators.LOCATOR_FILTER)
        self.check_element_enabled(GDSeacrhLocators.TYPELIST)
        self.check_element_enabled(GDSeacrhLocators.TOPICLIST)

    @allure.step("Expand topic list")
    def click_on_topictils(self):
        self.move_to_element(GDSeacrhLocators.TOPICLIST)
        self.find_element(GDSeacrhLocators.TOPICLIST).click()

    @allure.step("Select topic from Filter dropdown list")
    def select_article_from_dropdown(self):
        self.find_element(GDSeacrhLocators.CLOUD_AND_DEVOPS_TOPIC).click()

    @allure.step("Check amount of articles on page")
    def check_amount_of_articles(self):
        elements = self.find_elements(GDSeacrhLocators.ARTICLES_COUNT)
        assert len(elements) > 1, "There is less than 1 article"

    @allure.step("Reset filter")
    def reset_filter(self):
        self.find_element(GDSeacrhLocators.TOPICLIST).click()
        self.find_element(GDSeacrhLocators.ALL_TOPICS).click()

    @allure.step("Get first article on page after using filter")
    def get_first_article_on_page_after_using_filter(self):
        element = self.find_element(GDSeacrhLocators.FIRST_ARTICLE_AFTER_APPLYING_FILTER)
        return element.text.split('\n')

    @allure.step("Get article from topic list")
    def get_article(self):
        element = self.find_element(GDSeacrhLocators.FIRST_ARTICLE_BY_DEFAULT)
        return element.text.split('\n')

    @allure.step("Check the first article in list is different than previous and check there is more than 1 article")
    def compare_articles(self, get_article_before, get_article_after):
        if get_article_before and get_article_after is not "" or None:
            assert get_article_before != get_article_after, "Topics doesn't change"

    @allure.step("Click on Touch button")
    def click_get_in_touch(self):
        self.find_element(GDSeacrhLocators.GET_IN_TOUCH_BUTTON).click()

    @allure.step("Ensure page Contact Us opened")
    def check_get_in_touch_is_opened(self):
        assert self.driver.current_url == "https://www.griddynamics.com/contact", f"You are not in Get In Touch page," \
                                                                            f"current url is {self.driver.current_url}"
        self.check_element_is_presented(GDSeacrhLocators.QUESTION_FORM, time=5)

    @allure.step("Input data to Name field")
    def fill_question_form_name(self, text):
        self.input_data(GDSeacrhLocators.FIRST_NAME, text)

    @allure.step("Input data to Second Name field")
    def fill_question_form_last_name(self, text):
        self.input_data(GDSeacrhLocators.LAST_NAME, text)

    @allure.step("Input data to EMAIL field")
    def fill_question_form_email(self, text):
        self.input_data(GDSeacrhLocators.EMAIL, text)

    @allure.step("Click on field Question 'How did you hear us?'")
    def open_how_did_you_hear_us_dropdown_menu(self):
        self.find_element(GDSeacrhLocators.HOW_DID_YOU_HEAR_ABOUT_US).click()

    @allure.step("Select data to Question 'How did you hear us?'")
    def select_how_did_you_hear_us_dropdown_menu(self):
        self.move_to_element(GDSeacrhLocators.ONLINE_ADS)
        self.find_element(GDSeacrhLocators.ONLINE_ADS).click()

    @allure.step("Set checkbox policy")
    def select_checkbox(self, checkbox):
        list_of_checkboxes = self.find_elements(GDSeacrhLocators.CHECKBOXES)
        if checkbox == "policy":
            list_of_checkboxes[0].click()
        else:
            list_of_checkboxes[1].click()

    @allure.step("Check contact button is not active")
    def check_contact_button_is_not_active(self):
        assert not self.check_element_is_clickable(GDSeacrhLocators.CONTACT_BUTTON), "Button 'Contact' is active"
