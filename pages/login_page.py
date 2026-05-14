import allure
from locators.forgot_password_locators import ForgotPassword
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginLocators()

    @allure.step("Подскролить до кнопки 'Восстановить пароль'")
    def scroll_to_recover_button(self):
        self.scroll_to_element(self.locators.button_forgot_pass)

    @allure.step("Кликнуть на кнопку 'Восстановить пароль'")
    def click_to_forgot_password(self):
        self.click(self.locators.button_forgot_pass)
        self.wait_visible(ForgotPassword.page_title_reset)

    @allure.step("Ввести почту")
    def set_email(self, email):
        self.wait_visible(LoginLocators.button_login)
        self.send_keys(self.locators.email_input, email)

    @allure.step("Ввести пароль")
    def set_password(self, password):
        self.send_keys(self.locators.password_input, password)

    @allure.step("Кликнуть на кнопку 'Войти")
    def click_to_login(self):
        self.click(self.locators.button_login)
        self.wait_invisible(self.locators.title_login)

    @allure.step("Получить заголовок Вход")
    def get_title_of_page(self):
        self.wait_visible(self.locators.title_login)
        return self.get_text(self.locators.title_login)
