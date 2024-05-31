import requests
import api_urls
import data
import allure

class CreateNewUserApi:

    @staticmethod
    @allure.step("Регистрация пользователя")
    def create_new_user(body):

        return requests.post(api_urls.CREATE_USER_URL, json=body, headers=data.headers)

class LoginApi:

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(body, save_token):

        return requests.post(api_urls.LOGIN_URL, json=body, headers={'Authorization': f'{save_token}'})


class GetIngredients:
    @staticmethod
    @allure.step("Получение ингредиентов")
    def get_ingredients():

        return requests.get(api_urls.GET_INGREDIENTS_URL, headers=data.headers)


class CreateOrder:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(body, save_token):

        return requests.post(api_urls.CREATE_ORDER_URL, json=body, headers={'Authorization': f'{save_token}'})


class GetListOfOrders:

    @staticmethod
    @allure.step("Получение списка заказов")
    def get_orders(save_token):

        return requests.get(api_urls.GET_LIST_OF_ORDERS_URL, headers={'Authorization': f'{save_token}'})


class DeleteNewUserApi:

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(save_token):

        return requests.delete(api_urls.DELETE_USER_URL, headers={'Authorization': f'{save_token}'})
