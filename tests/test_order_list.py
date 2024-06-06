from pages.order_list_page import OrderList
from pages.main_page import MainPage
from pages.main_menu_page import MainMenuPage
from pages.lichniy_kaninet_page import LichniyKabinet
import allure


class TestOrderList:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('проверка, что текст заказа содержит Слово Состав')
    def test_popup_by_click_on_order_pass(self, driver, default_user_create_user):
        main_page = MainPage(driver)
        main_page.open_main_menu_page(default_user_create_user)
        main_menu = MainMenuPage(driver)
        main_menu.go_to_lenta_zakazov(driver)
        element = OrderList(driver)
        result = element.popup_by_click_on_order(driver)
        assert result == 'Cостав'


    @allure.title('Наличие созданных заказов в истории заказов и в ленте заказов')
    @allure.description('Проверка, что при создании заказа, заказ с таким номером есть в Истории заказа пользователя')
    def test_new_orders_in_order_history_displayed_in_order_list(self, driver, create_default_order):
        main_page = MainPage(driver)
        order_id = main_page.create_default_order_and_return_order_id(create_default_order)
        main_menu = MainMenuPage(driver)
        main_menu.go_to_lenta_zakazov(driver)
        order_list = OrderList(driver)
        order_list.search_element_by_order_number(order_id) # В search_element_by_order_number(order_id) проверяется, что заказ есть в Ленте заказов. Если заказа нет, то тест падает
        lihn_kab = LichniyKabinet(driver)
        lihn_kab.open_lichniy_kabinet_page(driver)
        order_id_2 = order_list.new_orders_in_order_history()
        assert str(order_id) in order_id_2


    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Проверка, что заказ созданный для пользоватея есть на странице Ленты заказов В работе')
    def test_quantity_of_all_new_orders_counter_raise(self, driver, default_user_create_user, get_ingredients):
        element = OrderList(driver)
        element_old = element.quantity_of_all_new_orders()
        main_page = MainPage(driver)
        main_page.create_default_order_helper(default_user_create_user, get_ingredients)
        element_new = element.quantity_of_all_new_orders()
        assert int(element_new) > int(element_old)


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('Проверка, что значение счетчика СЕГОДНЯШНИХ заказов было меньше до создания нового заказа')
    def test_quantity_of_all_today_orders_counter_raise(self, driver, default_user_create_user, get_ingredients):
        element = OrderList(driver)
        element_old = element.quantity_of_today_new_orders()
        main_page = MainPage(driver)
        main_page.create_default_order_helper(default_user_create_user, get_ingredients)
        element_new = element.quantity_of_today_new_orders()
        assert int(element_new) > int(element_old)


    @allure.title('При создании нового заказа номер заказа появляется в разделе В работе')
    def test_number_of_order_in_work_pass(self, driver, create_default_order):
        element = OrderList(driver)
        result = element.number_of_order_in_work(create_default_order)
        assert int(result[1]) == int(result[0])