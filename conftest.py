import pytest
from selenium import webdriver
from helper import UserFactory
from api import *
import allure

@allure.step("Запуск браузера")
@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':

        driver = webdriver.Chrome()
    elif request.param == 'firefox':


        driver = webdriver.Firefox()

    yield driver
    driver.quit()


@allure.step("Создание дофолтных параметров для пользователя")
@pytest.fixture(scope='function')
def default_user_create_data():
    data = UserFactory.create_user_with_random_param()
    return data


@allure.step("Создание дофолтного пользователя")
@pytest.fixture(scope='function')
def default_user_create_user(default_user_create_data):
    save_token = CreateNewUserApi.create_new_user(default_user_create_data).json()["accessToken"]
    yield [save_token, default_user_create_data]
    DeleteNewUserApi.delete_user(save_token)


@allure.step("Получение ингредиентов: вывод [список ингредиентов 2,1,5]")
@pytest.fixture(scope='function')
def get_ingredients():
    response = GetIngredients.get_ingredients()
    id_1 = response.json()['data'][1]['_id']
    id_2 = response.json()['data'][2]['_id']
    id_5 = response.json()['data'][5]['_id']
    dict_of_ingredients = {'ingredients': [id_2, id_1, id_5]}
    return dict_of_ingredients


@allure.step("Создание заказа: вывод [токен, ответ]")
@pytest.fixture(scope='function')
def create_default_order(default_user_create_user, get_ingredients):
    save_token = default_user_create_user[0]
    ingredients_data = get_ingredients
    response = CreateOrder.create_order(ingredients_data, save_token)
    yield [save_token, response.json(), default_user_create_user[1]]
    DeleteNewUserApi.delete_user(save_token)


