import allure

from task_selenium.pages.about_page import AboutPage
from task_selenium.pages.main_page import MainPage


class TestGridDynamics:

    @allure.feature("Check About page")
    def test_about_page(self, browser):
        main_page = MainPage(browser)
        about_page = AboutPage(browser)
        with allure.step("1"):
            main_page.go_to_url()
        with allure.step("2"):
            main_page.click_about()
        with allure.step("3"):
            about_page.click_on_person()
        with allure.step("4"):
            about_page.check_person_information()

    @allure.feature("Check Filter feature")
    def test_filter(self, browser):
        main_page = MainPage(browser)
        with allure.step("1"):
            main_page.go_to_url()
        with allure.step("2"):
            main_page.check_filter_presented_and_available()
        with allure.step("3"):
            main_page.click_on_topictils()
            main_page.select_article_from_dropdown()
        with allure.step("4"):
            main_page.check_amount_of_articles()
            get_article_before = main_page.get_first_article_on_page_after_using_filter()
        with allure.step("5"):
            main_page.reset_filter()
        with allure.step("6"):
            get_article_after = main_page.get_article()
            main_page.compare_articles(get_article_before, get_article_after)

    @allure.feature("Check filling data")
    def test_check_person_information(self, browser):
        main_page = MainPage(browser)
        with allure.step("1"):
            main_page.go_to_url()
        with allure.step("2"):
            main_page.click_get_in_touch()
        with allure.step("3"):
            main_page.check_get_in_touch_is_opened()
        with allure.step("4"):
            main_page.fill_question_form_name("Anna")
            main_page.fill_question_form_last_name("Smith")
            main_page.fill_question_form_email("annasmith@griddynamics.com")
            main_page.open_how_did_you_hear_us_dropdown_menu()
            main_page.select_how_did_you_hear_us_dropdown_menu()
        with allure.step("5"):
            main_page.select_checkbox(checkbox='policy')
        with allure.step("6"):
            main_page.select_checkbox(checkbox='allow')
        with allure.step("7"):
            main_page.check_contact_button_is_not_active()
