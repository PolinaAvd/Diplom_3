from locators.BL_locators_main_page import BasePageLocators as BL
from pages.base_page import BasePage
from api import *


class MainPage(BasePage):

    @allure.step('Забрать регистрационные данные для нового пользователя'
                'Открыть страницу авторизации'
                'Ввести емейл'
                'Ввести пароль'
                'Нажать вход'
                'Дождаться загрузки главной страницы')
    def open_main_menu_page(self, default_user_create_user):
        new_user_data = default_user_create_user[1]
        self.open_page(api_urls.AUTHORIZATION_PAGE_URL)
        self.find_element(BL.EMAIL_FIELD).send_keys(new_user_data['email'])
        self.find_element(BL.PASS_FIELD).send_keys(new_user_data['password'])
        self.go_to_element_and_click(BL.ENTER_BUTTON)
        start_page = self.find_element(BL.VISIBLE_COMPONENT_ON_MAIN)
        return start_page


    @allure.step('С помощью фикстры default_user_create_user, get_ingredients создать пользователя и параметры ингредиентов'
                 'Создать заказ'
                 'Удалить пользователя')
    def create_default_order_helper(self, default_user_create_user, get_ingredients):
        save_token = default_user_create_user[0]
        ingredients_data = get_ingredients
        CreateOrder.create_order(ingredients_data, save_token)
        DeleteNewUserApi.delete_user(save_token)

