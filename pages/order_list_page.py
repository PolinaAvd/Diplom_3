import allure
from pages.base_page import BasePage
import api_urls
from locators.LOL_locators_order_list import OrderListLocators as LOL



class OrderList(BasePage):


    @allure.step('Дождаться видимости элемента Заказ'
                 'Найти и перейти по Кнопке Заказ'
                 'Получить текст заказа')
    def popup_by_click_on_order(self):
        self.find_element(LOL.ORDER)
        self.go_to_element_and_click(LOL.ORDER)
        return self.get_text(LOL.CONSIST_TEXT)


    @allure.step('Поиск элемента по номеру заказа - метод для new_orders_in_order_history()')
    def search_element_by_order_number(self, num_order):
            str_num_order = LOL.ORDERS_LIST
            str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
            return self.find_element(str_num_order)


    @allure.step('Дождаться загрузки Истории заказов'
                 'Найти и нажать на Историю заказов'
                 'Забрать номер заказа order_id_2')
    def new_orders_in_order_history(self):
        self.find_element(LOL.ORDER_HISTORY_BUTTON)
        self.go_to_element_and_click(LOL.ORDER_HISTORY_BUTTON)
        order_id_2 = self.get_text(LOL.ORDER_NUMBER)
        return order_id_2


    @allure.step('Открыть Ленту заказов'
                 'Забрать старое количество заказов за все время')
    def quantity_of_all_new_orders(self):
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        number = self.get_text(LOL.ALL_TIME_ORDERS)
        return number


    @allure.step('Открыть Ленту заказов'
                 'Забрать старое количество заказов за СЕГОДНЯ')
    def quantity_of_today_new_orders(self):
        self.open_page(api_urls.LENTA_ZAKAZOV_URL)
        number = self.get_text(LOL.TODAY_ORDERS)
        return number


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
