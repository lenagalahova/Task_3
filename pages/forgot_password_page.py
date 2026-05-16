import allure
from locators.forgot_password_locators import ForgotPassword
from pages.base_page import BasePage


class ForgotPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPassword()

    @allure.step("Получить заголовок Восстановление пароля")
    def get_title_of_page(self):
        return self.get_text(self.locators.page_title_reset)

    @allure.step("Кликнуть на поле почты")
    def click_to_email(self):
        self.click(self.locators.input_email_forgot)

    @allure.step("Ввести почту")
    def set_email(self, email):
        self.send_keys(self.locators.input_email_forgot_active, email)

    @allure.step("Кликнуть на кнопку 'Восстановить'")
    def click_to_button_recover(self):
        self.click(self.locators.button_recover)

    @allure.step("Кликнуть на кнопку глаза")
    def click_to_eye_button(self):
        self.clickable(self.locators.eye_icon)
        self.click(self.locators.eye_icon)

    @allure.step("Подождать видимости активного поля пароля")
    def wait_visible_active_input(self):
        self.wait_visible(self.locators.active_input)

    @allure.step("Получить текст кнопки Сохранить")
    def get_text_of_button_save(self):
        return self.get_text(self.locators.button_save)

    @allure.step("Проверить, что пароль стал видимым (поле активно)")
    def is_password_field_active(self):
        active_container = self.find_element(self.locators.active_input)
        return active_container.is_displayed()
