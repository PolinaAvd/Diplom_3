import allure
from pages.base_page import BasePage
import api_urls
from locators.LOL_locators_order_list import OrderListLocators as LOL
from locators.LMM_locators_main_menu_page import MainMenuLocators as LMM
from locators.LLK_locators_lichniy_kabinet import LichniyKabinetLocators as LLK
from locators.BL_locators_main_page import BasePageLocators as BL


class OrderList(BasePage):


    @allure.step('Создание и авторизация нового пользователя методом open_main_menu_page()'
                 'Найти и перейти по кнопкеЛента Заказов'
                 'Дождаться видимости элемента Заказ'
                 'Найти и перейти по Кнопке Заказ'
                 'Получить текст заказа')
    def popup_by_click_on_order(self, default_user_create_user):
        self.open_main_menu_page(default_user_create_user)
        self.go_to_element_and_click(LMM.BUTTON_LENTA_ZAKAZOV)
        self.find_element(LOL.ORDER)
        self.go_to_element_and_click(LOL.ORDER)
        return self.get_text(LOL.CONSIST_TEXT)


    @allure.step('Поиск элемента по номеру заказа - метод для new_orders_in_order_history()')
    def search_element_by_order_number(self, num_order):
            str_num_order = LOL.ORDERS_LIST
            str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
            return self.find_element(str_num_order)


    @allure.step('С помощью фикстры create_default_order создать пользователя и заказ'
                 'Закбрать номер заказа пользователя order_id'
                 'Забрать логин и пароль пользователя'
                 'Открыть страницу автоизации'
                 'Ввести емейл'
                 'Ввести пароль'
                 'Нажать Вход'
                 'Дождться загрузки главной страницы'
                 'Нажать кнопку Лента заказов'
                 'Найти элемент пономеру заказа из заказ, созданного через апи метод'
                 'Найи и перейти по кнопке ЛК'
                 'Дождаться загрузки Истории заказов'
                 'Найти и нажать на Историю заказов'
                 'Забрать номер заказа order_id_2')
    def new_orders_in_order_history(self, create_default_order):
        order = create_default_order[1]
        order_id = order['order']['number']
        login_data = create_default_order[2]
        self.open_page(api_urls.AUTHORIZATION_PAGE_URL)
        self.driver.find_element(*BL.EMAIL_FIELD).send_keys(login_data['email'])
        self.driver.find_element(*BL.PASS_FIELD).send_keys(login_data['password'])
        self.go_to_element_and_click(BL.ENTER_BUTTON)
        self.find_element(BL.VISIBLE_COMPONENT_ON_MAIN)
        self.go_to_element_and_click(LMM.BUTTON_LENTA_ZAKAZOV)
        self.search_element_by_order_number(order_id) # В search_element_by_order_number(order_id) проверяется, что заказ есть в Ленте заказов. Если заказа нет, то тест падает
        self.go_to_element_and_click(LLK.LICHN_KABINET)
        self.find_element(LOL.ORDER_HISTORY_BUTTON)
        self.go_to_element_and_click(LOL.ORDER_HISTORY_BUTTON)
        order_id_2 = self.get_text(LOL.ORDER_NUMBER)
        return [order_id, order_id_2]


    @allure.step('Открыть Ленту заказов'
                 'Забрать старое количество заказов за все время old_number'
                 'Прогнать создание заказа create_default_order_helper()'
                 'Открыть Ленту заказов'
                 'Забрать новое количество заказов new_number')
    def quantity_of_all_new_orders(self, default_user_create_user, get_ingredients):
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        old_number = self.get_text(LOL.ALL_TIME_ORDERS)
        self.create_default_order_helper(default_user_create_user, get_ingredients)
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        new_number = self.get_text(LOL.ALL_TIME_ORDERS)
        return [old_number, new_number]


    @allure.step('Открыть Ленту заказов'
                 'Забрать старое количество заказов за СЕГОДНЯ old_number'
                 'Прогнать создание заказа create_default_order_helper()'
                 'Открыть Ленту заказов'
                 'Забрать новое количество заказов new_number')
    def quantity_of_today_new_orders(self, default_user_create_user, get_ingredients):
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        old_number = self.get_text(LOL.TODAY_ORDERS)
        self.create_default_order_helper(default_user_create_user, get_ingredients)
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        new_number = self.get_text(LOL.TODAY_ORDERS)
        return [old_number, new_number]


    @allure.step('С помощью фикстры create_default_order создать пользователя и заказ'
                 'Открыть Ленту заказов'
                 'Забрать параметр с номером заказа, созданный методом API'
                 'Забрать значение номера заказа'
                 'Получить тескт заказов в работе на странице')
    def number_of_order_in_work(self, create_default_order):
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        order = create_default_order[1]
        order_id = order['order']['number']
        order_on_the_page = self.get_text(LOL.ORDERS_IN_WORK)
        return [order_id, order_on_the_page]
