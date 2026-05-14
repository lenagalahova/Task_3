import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import email, password
from pages.order_feed_page import OrderFeedPage


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestMainFunction:
    @allure.title("Проверка перехода на страницу «Конструктор»")
    def test_cross_to_constructor_page(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажать на «Конструктор»"):
            main_page.click_to_constructor()
            text = main_page.get_title_of_page()
            assert "Соберите бургер" in text

    @allure.title("Проверка перехода на страницу «Лента заказов»")
    def test_cross_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Нажать на Лента заказов"):
            main_page.click_to_order_feed()
            current_url = order_feed.get_current_url()
            assert "/feed" in current_url

    @allure.title(
        "Проверка появления всплывающего окна с деталями, если кликнуть на ингредиент"
    )
    def test_popup_with_ditails(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажать на булку"):
            main_page.click_to_bun()
            text = main_page.get_title_of_popup()
            assert "Детали ингредиента" in text

    @allure.title("Проверка закрытия попапа кликом по крестику")
    def test_close_popup_with_ditails(self, driver):
        main_page = MainPage(driver)

        with allure.step("Нажать на булку"):
            main_page.click_to_bun()
        with allure.step("Нажать на крестик"):
            main_page.click_to_button_close()
        with allure.step("Проверить невидимость попапа"):
            main_page.is_invisibility_popap()
        assert True

    @allure.title(
        "Проверка что при добавлении ингредиента в заказ, увеличивается каунтер"
    )
    def test_add_ingredient_and_raise_counter(self, driver):

        main_page = MainPage(driver)
        with allure.step("Получить начальное значение счетчика"):
            text0 = main_page.get_text_counter()
            text_number_0 = int(text0)

        with allure.step("Добавить булку в заказ"):
            main_page.drag_ingredient_to_constructor()

        with allure.step("Получить новое значение счетчика"):
            text1 = main_page.get_text_counter()
            text_number_1 = int(text1)

        with allure.step("Проверить, что счетчик увеличился"):
            assert text_number_1 > text_number_0

    @allure.title("Проверка что залогиненный пользователь может оформить заказ")
    def test_take_order_of_auth_user(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Добавить булку в заказ и нажать на Войти в аккаунт"):
            main_page.drag_ingredient_to_constructor()
            main_page.click_to_make_order()
        with allure.step("Вход в Личный кабинет"):
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
        with allure.step("Нажать на кнопку Сделать заказ"):
            main_page.click_to_make_order()
            text = main_page.get_text_of_starting_make_order()
        assert "Ваш заказ начали готовить" in text
