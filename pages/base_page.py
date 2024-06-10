from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from api import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)


    @allure.step('Перемеcтиться до элемента и кликнуть')
    def go_to_element_and_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    @allure.step('Перенос элемента')
    def drag_and_drop(self, element, target):
        return ActionChains(self.driver).drag_and_drop(element, target).pause(5).perform()


    @allure.step('Собрать текст с элемента')
    def get_text(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator)).text


    @allure.step('Проверяем видимость элемента')
    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))


    @allure.step('Вернуть url')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Вернуть page_source')
    def get_page_source(self):
        return self.driver.page_source







