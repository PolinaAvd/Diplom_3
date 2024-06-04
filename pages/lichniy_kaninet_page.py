import allure
from locators.LLK_locators_lichniy_kabinet import LichniyKabinetLocators as LLK
from pages.base_page import BasePage


class LichniyKabinet(BasePage):


    @allure.step('Авторизоваться методом open_main_menu_page()'
                 'Найти и перейти в ЛК'
                 'Дождаться загрузки Кнопки Сохранить в ЛК')
    def open_lichniy_kabinet_page(self, default_user_create_user):
        self.open_main_menu_page(default_user_create_user)
        self.go_to_element_and_click(LLK.LICHN_KABINET)
        self.find_element(LLK.SOHRANIT_V_LICHN_KAB)
        return self.driver


    @allure.step('Перейти в ЛК методом open_lichniy_kabinet_page()'
                 'Найти и перейти по кнопке История заказов')
    def go_to_history_of_orders(self, default_user_create_user):
        self.open_lichniy_kabinet_page(default_user_create_user)
        self.go_to_element_and_click(LLK.KNOPKA_ISTORIYA_ZAKAZOV)
        return self.driver


    @allure.step('Перейти в ЛК методом open_lichniy_kabinet_page()'
                'Найти кнопку Выход и нажать'
                 'Дождаться видимости кнопки Вход на странице регистрации')
    def exit_lichniy_kabinet(self, default_user_create_user):
        self.open_lichniy_kabinet_page(default_user_create_user)
        self.go_to_element_and_click(LLK.KNOPKA_VIHOD)
        self.find_element(LLK.ENTER_BUTTON)
        return self.driver

