from pages.order_list_page import OrderList
import allure


class TestOrderList:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('проверка, что текст заказа содержит Слово Состав')
    def test_popup_by_click_on_order_pass(self, driver, default_user_create_user):
        element = OrderList(driver).popup_by_click_on_order(driver, default_user_create_user)
        assert element == 'Cостав'


    @allure.title('Наличие созданных заказов в истории заказов и в ленте заказов')
    @allure.description('Проверка, что при создании заказа, заказ с таким номером есть в Истории заказа пользователя')
    def test_new_orders_in_order_history_displayed_in_order_list(self, driver, create_default_order):
        element = OrderList(driver).new_orders_in_order_history(create_default_order)
        assert str(element[0]) in element[1]


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Проверка, что заказ созданный для пользоватея есть на странице Ленты заказов В работе')
    def test_quantity_of_all_new_orders_counter_raise(self, driver, default_user_create_user, get_ingredients):
        element = OrderList(driver).quantity_of_all_new_orders(default_user_create_user, get_ingredients)
        assert int(element[1]) > int(element[0])


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверка, что значение счетчика СЕГОДНЯШНИХ заказов было меньше до создания нового заказа')
    def test_quantity_of_all_today_orders_counter_raise(self, driver, default_user_create_user, get_ingredients):
        element = OrderList(driver).quantity_of_today_new_orders(default_user_create_user, get_ingredients)
        assert int(element[1]) > int(element[0])


    @allure.title('При создании нового заказа номер заказа появляется в разделе В работе')
    def test_number_of_order_in_work_pass(self, driver, create_default_order):
        element = OrderList(driver).number_of_order_in_work(create_default_order)
        assert int(element[1]) == int(element[0])