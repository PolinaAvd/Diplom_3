from pages.lichniy_kaninet_page import LichniyKabinet
import api_urls
import allure

class TestLichniyKabinet:

    @allure.title('Переход по клику на «Личный кабинет»')
    @allure.description('Проверка текущего url - совпадает с url ЛК')
    def test_open_lichniy_kabinet_page_pass(self, driver, default_user_create_user):
        element = LichniyKabinet(driver)
        result = element.open_lichniy_kabinet_page(driver, default_user_create_user)
        assert result == api_urls.LICHNIY_KABINET_URL


    @allure.title('Переход в раздел «История заказов»')
    @allure.description('Проверка текущего url - совпадает с url стриницы История заказов')
    def test_go_to_history_of_orders_pass(self, driver, default_user_create_user):
        element = LichniyKabinet(driver)
        result = element.go_to_history_of_orders(driver, default_user_create_user)
        assert result == api_urls.ORDERS_HISTORY_URL


    @allure.title('Выход из ЛК')
    @allure.description('Проверка текущего url - совпадает с url стриницы Авторизации')
    def test_exit_lichniy_kabinet_pass(self, driver, default_user_create_user):
        element = LichniyKabinet(driver)
        result = element.exit_lichniy_kabinet(driver, default_user_create_user)
        assert result == api_urls.AUTHORIZATION_PAGE_URL
