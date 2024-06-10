import allure
from pages.base_page import BasePage
from locators.LMM_locators_main_menu_page import MainMenuLocators as LMM
import api_urls



class MainMenuPage(BasePage):


    @allure.step('Поиск и клик по кнопке Конструктор')
    def click_on_konstruktor(self):
        self.go_to_element_and_click(LMM.BUTTON_KONSTRUKTOR)


    @allure.step('Поиск кнопки Лента заказов и переход по ней')
    def go_to_lenta_zakazov(self):
        self.go_to_element_and_click(LMM.BUTTON_LENTA_ZAKAZOV)


    @allure.step('Открыть главную страницу'
                 'Найти ингредиент и кликнуть по нему'
                 'Получить код страницы')
    def click_on_ingredients(self):
        self.open_page(api_urls.MAIN_PAGE_URL)
        self.go_to_element_and_click(LMM.INGREDIENT)
        return self.get_page_source()


    @allure.step('Клик по ингредиенту из метода click_on_ingredients()'
                 'Поиск и клик по кнопке Закрыть всплывающее окно'
                 'Получить код страницы')
    def click_on_ingredients_and_close(self):
        self.click_on_ingredients()
        self.go_to_element_and_click(LMM.CLOSE_BUTTON)
        return self.get_page_source()


    @allure.step('Открыть главную страницу'
                 'Нажать на ингредиент и перетащить его в Конструктор заказа методом drag_and_drop()'
                 'Получить текст счетчика ингредиентов')
    def click_on_ingredients_and_drop_to_basket(self):
        self.open_page(api_urls.MAIN_PAGE_URL)
        self.drag_and_drop(self.find_element(LMM.INGREDIENT), self.find_element(LMM.BURGER_CONSTRUCTOR))
        return self.get_text(LMM.INGREDIENT_COUNTER)


    @allure.step('Создание и авторизация нового пользователя методом open_main_menu_page()'
                 'Нажать на ингредиент и перетащить его в Конструктор заказа методом drag_and_drop()'
                 'Найти и перейти по кнопке Заказать'
                 'Дождаться видимости текста заказа'
                 'Получить текст Заказа')
    def make_order(self):
        self.drag_and_drop(self.find_element(LMM.INGREDIENT), self.find_element(LMM.BURGER_CONSTRUCTOR))
        self.go_to_element_and_click(LMM.ORDER_BUTTON)
        self.find_element(LMM.ORDER_TEXT)
        return self.get_text(LMM.ORDER_TEXT)



