from selenium.webdriver.common.by import By

class ResetPassLocators:


    LINK_VOSSTANANOVIT_PASS = (By.XPATH, ".//p[2]/a[text()='Восстановить пароль']") # Ссылка на Восстановить пароль на странице /login
    BUTTON_VOSSTANOVIT_PASS = (By.XPATH, ".//form[@class='Auth_form__3qKeq mb-20']//button[text()='Восстановить']")  # Кнопка Восстановить пароль на странице /forgot-password
    VVEDITE_KOD_IZ_PISMA = (By.XPATH, ".//div[@class='input__container']//label[text()='Введите код из письма']")  # Кнопка Введите код из письма на странице /forgot-password
    VVEDITE_NOVIJ_PASS = (By.XPATH, ".//div[@class='input__container']//input[@name='Введите новый пароль']") # Кнопка Введите новый пароль на странице /reset-password
    EYE_BUTTON = (By.XPATH, "//div[@class='input__icon input__icon-action']") # Кнопка с глазом на странице /reset-password

