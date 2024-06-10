from pages.lichniy_kaninet_page import LichniyKabinet
from pages.main_page import MainPage
import api_urls
import allure

class TestLichniyKabinet:

    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверка текущего url - совпадает с url ЛК')
    def test_open_lichniy_kabinet_page_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        element = LichniyKabinet(driver)
        element.open_lichniy_kabinet_page()
        assert element.get_current_url() == api_urls.LICHNIY_KABINET_URL


    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверка текущего url - совпадает с url стриницы История заказов')
    def test_go_to_history_of_orders_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        element = LichniyKabinet(driver)
        element.go_to_history_of_orders()
        assert element.get_current_url() == api_urls.ORDERS_HISTORY_URL


    @allure.title('Выход из ЛК')
    @allure.description('Проверка текущего url - совпадает с url стриницы Авторизации')
    def test_exit_lichniy_kabinet_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        element = LichniyKabinet(driver)
        element.exit_lichniy_kabinet()
        assert element.get_current_url() == api_urls.AUTHORIZATION_PAGE_URL
