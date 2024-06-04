import data
from pages.main_menu_page import MainMenuPage
import api_urls
import allure

class TestMainMenu:

    @allure.title('Переход по кнопке Конструктор')
    @allure.description('Проверка текущего url - совпадает с url страницы Авторизации')
    def test_go_to_konstruktor_pass(self, driver, default_user_create_user):
        element = MainMenuPage(driver).go_to_konstruktor(driver, default_user_create_user)
        assert element == api_urls.MAIN_PAGE_URL + '/'


    @allure.title('Переход в Ленту заказов')
    @allure.description('Проверка текущего url - совпадает с url страницы Лента заказов')
    def test_go_to_lenta_zakazov_pass(self, driver, default_user_create_user):
        element = MainMenuPage(driver).go_to_lenta_zakazov(driver, default_user_create_user)
        assert element == api_urls.LENTA_ZAKAZOV_URL


    @allure.title('Клик по ингредиенту в Главном меню')
    @allure.description('Проверка, что в коде страницы есть элемент, с деталями игредиента')
    def test_click_on_ingredients_pass(self, driver):
        element = MainMenuPage(driver).click_on_ingredients()
        assert data.DETALI_INGREDIENTA_VISIBLE in element


    @allure.title('Клик закрыть в открытом окне с Деталями ингредиента')
    @allure.description('Проверка, что в коде страницы нет элемента, с деталями игредиента')
    def test_click_on_ingredients_and_close_pass(self, driver):
        element = MainMenuPage(driver).click_on_ingredients_and_close()
        assert data.DETALI_INGEDIENTA_INVISIBLE in element


    @allure.title('Перетащить ингредиент в корзину')
    @allure.description('Проверка счетчика ингредиентов: увеличивается. Note: Для Firefox тест не стабилен: проблема FF и метода drag_and_drop()')
    def test_click_on_ingredients_and_drop_to_basket_pass(self, driver):
        element = MainMenuPage(driver).click_on_ingredients_and_drop_to_basket()
        assert element == '2'


    @allure.title('Офомить заказ для авторизованного пользователя')
    @allure.description('Проверка: Есть идентификатор заказа')
    def test_make_order_pass(self, driver, default_user_create_user):
        element = MainMenuPage(driver).make_order(driver, default_user_create_user)
        assert element == 'идентификатор заказа'