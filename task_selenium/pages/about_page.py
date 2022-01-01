import allure

from task_selenium.pages.base_action import BaseAction
from task_selenium.pages.locators import GDSeacrhLocators


class AboutPage(BaseAction):

    @allure.step("Click on person Leonard")
    def click_on_person(self):
        self.find_elements(GDSeacrhLocators.NAME_LEONARD)[0].click()

    @allure.step("Verify information about person")
    def check_person_information(self):
        self.check_element_is_presented(GDSeacrhLocators.PERSON_MODAL_WRAPPER)
        get_position = self.find_element(GDSeacrhLocators.PERSON_DETAILS).text.replace('\n', " ")
        assert "Leonard Livschitz CHIEF EXECUTIVE OFFICER AND DIRECTOR" == get_position, "Person information is wrong"
        get_text = self.find_element(GDSeacrhLocators.PERSON_DESCRIPTION).text
        assert "board of directors since 2006 and the Chief Executive Officer of Grid Dynamics since 2014" in get_text,\
               "Describing of positions is wrong"