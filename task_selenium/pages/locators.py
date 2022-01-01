
from selenium.webdriver.common.by import By


class GDSeacrhLocators:
    ABOUT = (By.XPATH, "//a[contains(text(), 'About')]")
    NAME_LEONARD = (By.XPATH, "//*[@class='name' and contains(text(),'Leonard')]")
    LOCATOR_FILTER = (By.ID, "filters")
    PERSON_MODAL_WRAPPER = (By.CLASS_NAME, "modal-wrapper")
    PERSON_DETAILS = (By.CLASS_NAME, "details")
    PERSON_DESCRIPTION = (By.XPATH, "//span[contains(text(), 'board of directors since 2006 "
                                    "and the Chief Executive Officer of Grid Dynamics since 2014.')]")
    TYPELIST = (By.ID, "typelist")
    TOPICLIST = (By.ID, "topiclist")
    SELECTED_ARTICLE_ON_PAGE_FILTER = (By.XPATH, "//span[contains(@class, 'selected') and contains "
                                                 "(., 'Cloud and DevOps')]")
    FIRST_ARTICLE_AFTER_APPLYING_FILTER = (By.XPATH, "//*[@id='woe']/section[8]/div/div[1]/a/article/div/h4")
    FIRST_ARTICLE_BY_DEFAULT = (By.XPATH, "//*[@id='woe']/section[4]/div/div[1]/a/article/div/h4")
    CLOUD_AND_DEVOPS_TOPIC = (By.XPATH, "//span[@data-value='cloud-and-devops']")
    ARTICLES_COUNT = (By.TAG_NAME, "article")
    ALL_TOPICS = (By.XPATH, "//span[contains(@data-value, 'all') and contains (., 'All topics')]")
    # GET_IN_TOUCH_BUTTON = (By.CSS_SELECTOR, "#woe > gd-header > header > div > div > a.contact-button."
    #                                         "ui-button-standard.ui-button.ui-button-size-default")
    GET_IN_TOUCH_BUTTON = (By.CSS_SELECTOR, "#woe > gd-header > header > div > div"
                                            " > a.contact-button.ui-button-standard.ui-button.ui-button-size-default "
                                            "> span.ui-button-wrapper.ui-button-block")
    QUESTION_FORM = (By.XPATH, "//*[@class='gd-container ng-star-inserted']")
    FIRST_NAME = (By.XPATH, "//*[@placeholder='First name*']")
    LAST_NAME = (By.XPATH, "//*[@placeholder='Last name*']")
    EMAIL = (By.XPATH, "//*[@placeholder='E-mail*']")

    HOW_DID_YOU_HEAR_ABOUT_US = (By.XPATH, "//*[contains(text(), 'How did you hear about us?')]")
    ONLINE_ADS = (By.XPATH, "//*[contains(text(), ' Online Ads ')]")
    CHECKBOXES = (By.XPATH, "//span[@class='gd-checkbox-field-legacy__icon']")
    CONTACT_BUTTON = (By.XPATH, "//div[@class='gd-centered-block submit-button']")
