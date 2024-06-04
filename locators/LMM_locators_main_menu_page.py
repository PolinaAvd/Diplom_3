from selenium.webdriver.common.by import By

class MainMenuLocators:


    BUTTON_KONSTRUKTOR = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка Конструктор на Главной странице
    BUTTON_LENTA_ZAKAZOV = (By.XPATH, ".//p[contains(text(),'Лента Заказов')]") # Кнопка Лента Заказов на Главной странице
    INGREDIENT = (By.XPATH, './/*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')  # Локатор для ингредиента на странице меню
    CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"close")]')  # Закрытие всплывающего окна с ингредиентом
    BURGER_CONSTRUCTOR = (By.XPATH, '//*[@class="BurgerConstructor_basket__list__l9dp_"]') # Конструктор бургеров
    INGREDIENT_COUNTER = (By.XPATH, '//*[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[contains(@class, "counter__num")]') # Счетчик ингредиентов
    ORDER_BUTTON = By.XPATH, '//button[contains(text(),"Оформить заказ")]' # Кнопка оформить  заказ
    ORDER_TEXT = By.XPATH, '//p[@class="undefined text text_type_main-medium mb-15"]' # ЛОкатор для текста заказа


