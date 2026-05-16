import time

import allure
import pytest
from pages.main_page import MainPage
from pages.forgot_password_page import ForgotPage
from pages.login_page import LoginPage
from data import email


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestForgotPassword:
    driver = None

    @allure.title(
        "Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»"
    )
    def test_cross_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
        with allure.step("Нажать Восстановление пароля"):
            login_page.scroll_to_recover_button()
            login_page.click_to_forgot_password()
            text = forgot_page.get_title_of_page()
        assert "Восстановление пароля" in text

    @allure.title("Проверка ввода почты и клик по кнопке «Восстановить»")
    def test_set_email_and_click_to_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
        with allure.step("Нажать восстановить пароль"):
            login_page.scroll_to_recover_button()
            login_page.click_to_forgot_password()
            forgot_page.click_to_email()
        with allure.step("Ввести почту"):
            forgot_page.set_email(email)
        with allure.step("Нажать восстановить пароль"):
            forgot_page.click_to_button_recover()
            text = forgot_page.get_text_of_button_save()
            assert "Сохранить" in text

    @allure.title("Проверка клика по глазу поля Пароль делает его активным")
    def test_click_to_eye_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        forgot_page = ForgotPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
        with allure.step("Нажать восстановить пароль"):
            login_page.scroll_to_recover_button()
            login_page.click_to_forgot_password()
        with allure.step("Ввести почту"):
            forgot_page.set_email(email)
        with allure.step("Нажать восстановить пароль"):
            forgot_page.click_to_button_recover()
        with allure.step("Нажать на глазик"):
            forgot_page.click_to_eye_button()
            forgot_page.wait_visible(forgot_page.locators.active_input)
            assert forgot_page.is_password_field_active()
