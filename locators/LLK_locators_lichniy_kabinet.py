from selenium.webdriver.common.by import By


class LichniyKabinetLocators:


    LICHN_KABINET = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']//p[text()='Личный Кабинет']") # Личный кабинет
    SOHRANIT_V_LICHN_KAB = (By.XPATH, ".//div[@class='Profile_profile__3dzvr']//button[text()='Сохранить']")  # Компонент, ло которого ожидается загрузка ЛК, кнопка Сохранить
    KNOPKA_ISTORIYA_ZAKAZOV = (By.XPATH, ".//a[text()='История заказов']") # Кнопка История заказов в ЛК
    KNOPKA_VIHOD =  (By.XPATH, ".//button[text()='Выход']") # Кнопка Выход из ЛК
    ENTER_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//button[text()='Войти']")  # Кнопка Войти на странице /login


