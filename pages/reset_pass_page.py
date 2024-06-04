import helper
import allure
from pages.base_page import BasePage
from locators.LRP_locators_reset_pass import ResetPassLocators as LRP
from locators.BL_locators_main_page import BasePageLocators as BL
import api_urls


class ResetPass(BasePage):


    @allure.step('Открываем страницу авторизации'
                 'Находим сслыку Восстановить пароль и кликаем по ней')
    def open_reset_pass_page(self):
        self.open_page(api_urls.AUTHORIZATION_PAGE_URL)
        self.go_to_element_and_click(LRP.LINK_VOSSTANANOVIT_PASS)
        return self.driver.current_url


    @allure.step('Переходим на страницу восстановления пароля'
                 'На странице восстановления пароля вводим емейл'
                 'Нажимаем восстановить пароль'
                 'Ожидание загрузки страницы с текстом Введите код из письма')
    def vosstanovit_pass_enter_email(self):
        self.open_reset_pass_page()
        self.find_element(BL.EMAIL_FIELD).send_keys(helper.email_random)
        self.find_element(LRP.BUTTON_VOSSTANOVIT_PASS).click()
        self.find_element(LRP.VVEDITE_KOD_IZ_PISMA)
        return self.driver.current_url


    @allure.step('Первые шаги из vosstanovit_pass_enter_email()'
                 'Ввод рандомного пароля'
                 'Нажатие на Глаз'
                 'Получение кода страницы')
    def check_pass_symbols_visible(self):
        self.vosstanovit_pass_enter_email()
        self.find_element(LRP.VVEDITE_NOVIJ_PASS).send_keys(helper.password_random)
        self.go_to_element_and_click(LRP.EYE_BUTTON)
        element = self.driver.page_source
        return element



