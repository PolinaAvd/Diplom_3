from selenium.webdriver.common.by import By

class OrderListLocators:


    BUTTON_LENTA_ZAKAZOV = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]") # Кнопка Лента Заказов на Главной странице
    ORDER = By.XPATH, ".//h2[@class='text text_type_main-medium mb-2']"
    CONSIST_TEXT = By.XPATH, '//p[text()="Cостав"]'
    ORDERS_LIST = By.XPATH, '//*[text()="#0{num_order}"]' # Номер закааза на странице заказов
    VISIBLE_COMPONENT_ON_MAIN = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//h1[@class='text text_type_main-large mb-5 mt-10']")  # Компонент, до к-рого ожидаем загрузку на главной странице
    ORDER_HISTORY_BUTTON = By.XPATH, '//a[contains(text(),"История заказов")]'
    ORDER_NUMBER = By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]'
    ALL_TIME_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "digits-large")]')
    TODAY_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "digits-large")]')
    ORDERS_IN_WORK = By.XPATH, '//*[contains(@class, "orderListReady")]//li[contains(@class, "digits-default")]'
    ALL_ORDERS_READY = By.XPATH, '//li[@class="text text_type_main-small"]'






