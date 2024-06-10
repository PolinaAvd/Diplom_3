import data
from pages.main_menu_page import MainMenuPage
from pages.main_page import MainPage
from pages.lichniy_kaninet_page import LichniyKabinet
import api_urls
import allure

class TestMainMenu:

    @allure.title('Переход по кнопке Конструктор')
    @allure.description('Проверка текущего url - совпадает с url страницы Авторизации')
    def test_go_to_konstruktor_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        lich_kab = LichniyKabinet(driver)
        lich_kab.open_lichniy_kabinet_page()
        element = MainMenuPage(driver)
        element.click_on_konstruktor()
        assert element.get_current_url() == api_urls.MAIN_PAGE_URL + '/'


    @allure.title('Переход в Ленту заказов')
    @allure.description('Проверка текущего url - совпадает с url страницы Лента заказов')
    def test_go_to_lenta_zakazov_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        element = MainMenuPage(driver)
        element.go_to_lenta_zakazov()
        assert element.get_current_url() == api_urls.LENTA_ZAKAZOV_URL


    @allure.title('Клик по ингредиенту в Главном меню')
    @allure.description('Проверка, что в коде страницы есть элемент, с деталями игредиента')
    def test_click_on_ingredients_pass(self, driver):
        element = MainMenuPage(driver)
        result = element.click_on_ingredients()
        assert data.DETALI_INGREDIENTA_VISIBLE in result


    @allure.title('Клик закрыть в открытом окне с Деталями ингредиента')
    @allure.description('Проверка, что в коде страницы нет элемента, с деталями игредиента')
    def test_click_on_ingredients_and_close_pass(self, driver):
        element = MainMenuPage(driver)
        result = element.click_on_ingredients_and_close()
        assert data.DETALI_INGEDIENTA_INVISIBLE in result


    @allure.title('Перетащить ингредиент в корзину')
    @allure.description('Проверка счетчика ингредиентов: увеличивается. Note: Для Firefox тест не стабилен: проблема FF и метода drag_and_drop()')
    def test_click_on_ingredients_and_drop_to_basket_pass(self, driver):
        element = MainMenuPage(driver)
        result = element.click_on_ingredients_and_drop_to_basket()
        assert result == '2'


    @allure.title('Офомить заказ для авторизованного пользователя')
    @allure.description('Проверка: Есть идентификатор заказа')
    def test_make_order_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        element = MainMenuPage(driver)
        result = element.make_order()
        assert result == 'идентификатор заказа'