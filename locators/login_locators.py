from selenium.webdriver.common.by import By


class LoginLocators:
    email_input = (By.XPATH, './/input[@name="name"]')
    password_input = (By.XPATH, './/input[@type="password"]')
    button_login = (By.XPATH, './/button[text()="Войти"]')
    button_register = (
        By.XPATH,
        './/button[@class = "Auth_link__1fOlj" and text()="Зарегистрироваться"]',
    )
    button_forgot_pass = (
        By.XPATH,
        './/a[@class = "Auth_link__1fOlj" and text()="Восстановить пароль"]',
    )
    title_login = (By.XPATH, './/h2[text()="Вход"]')
