from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from locators.BL_locators_main_page import BasePageLocators as BL
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


    @allure.step('С помощью фикстры default_user_create_user, get_ingredients создать пользователя и параметры ингредиентов'
                 'Создать заказ'
                 'Удалить пользователя')
    def create_default_order_helper(self, default_user_create_user, get_ingredients):
        save_token = default_user_create_user[0]
        ingredients_data = get_ingredients
        CreateOrder.create_order(ingredients_data, save_token)
        DeleteNewUserApi.delete_user(save_token)





