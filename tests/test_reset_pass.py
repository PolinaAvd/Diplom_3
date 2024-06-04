import data
from pages.reset_pass_page import ResetPass
import allure
import api_urls

class TestResetPass:

    @allure.title('Переход на страницу восстановления пароля по кнопке Восстановить пароль')
    @allure.description('Проверка текущего url открылась страница с Восстановлением пароля')
    def test_open_reset_pass_page_pass(self, driver):
        element = ResetPass(driver)
        result = element.open_reset_pass_page()
        assert result == api_urls.FORGOT_PASS_PAGE_URL


    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Проверка текущего url - reset-pass')
    def test_vosstanovit_pass_enter_email_pass(self, driver):
        element = ResetPass(driver)
        result = element.vosstanovit_pass_enter_email()
        assert result == api_urls.RESET_PASS_PAGE_URL


    @allure.title('Клик по кнопке показать/скрыть пароль')
    @allure.description('Проверка, что в коде страницы содержится элемент, отвечающий за подсветку пароля')
    def test_check_pass_symbols_visible_pass(self, driver):
        element = ResetPass(driver)
        result = element.check_pass_symbols_visible()
        assert data.PASS_IS_VISIBLE_ELEMENT_IN_HTML in result



