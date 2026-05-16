import allure
import pytest
from pages.lk_page import LKPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import email, password


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestLK:
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_cross_to_lk_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        lk_page = LKPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
            main_page.click_to_lk_button()
            current_url = lk_page.get_current_url()
            assert "/account" in current_url

    @allure.title("Проверка перехода в раздел «История заказов»")
    def test_cross_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        lk_page = LKPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
            main_page.click_to_lk_button()
        with allure.step("Переход в раздел История заказов"):
            lk_page.click_to_history()
            current_url = lk_page.get_current_url()
            assert "/account/order-history" in current_url

    @allure.title("Проверка выхода из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        lk_page = LKPage(driver)

        with allure.step("Вход в Личный кабинет"):
            main_page.click_to_lk_button()
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
            main_page.click_to_lk_button()
        with allure.step("Выход из ЛК"):
            lk_page.click_to_logout()
            text = login_page.get_title_of_page()
            assert "Вход" in text
