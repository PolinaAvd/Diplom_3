from selenium.webdriver.common.by import By


class BasePageLocators:

    EMAIL_FIELD = (By.XPATH, ".//div[@class='input__container']//input[@name='name']")  # Поле емэйл на странице /login
    PASS_FIELD = (By.XPATH, "//div[@class='input__container']//input[@name='Пароль']")  # Поле пароль на странице /login
    ENTER_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']")  # Кнопка Войти на странице /login
    VISIBLE_COMPONENT_ON_MAIN = (By.XPATH, "//main[@class='App_componentContainer__2JC2W']//h1[@class='text text_type_main-large mb-5 mt-10']")  # Компонент, до к-рого ожидаем загрузку на главной странице
