import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import email, password
from pages.order_feed_page import OrderFeedPage


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
class TestOrderFeed:
    driver = None

    @allure.title("Проверка открытие всплывающего окна с деталями при клике на заказ,")
    def test_cross_to_order_feed_page(self, driver):
        main_page = MainPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Нажать на Лента заказов"):
            main_page.click_to_order_feed()
            current_url = order_feed.get_current_url()
            assert "/feed" in current_url

        with allure.step("Нажать на заказ"):
            order_feed.click_to_order()
            assert order_feed.is_modal_window_opened()

    @allure.title("Заказы пользователя из истории отображаются в ленте заказов")
    def test_user_orders_displayed_in_order_feed(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Добавить булку в заказ и нажать на Войти в аккаунт"):
            main_page.drag_ingredient_to_constructor()
            main_page.click_to_make_order()
        with allure.step("Вход в Личный кабинет"):
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
        with allure.step("Сделать заказ"):
            main_page.click_to_make_order()
            main_page.wait_clickable_close_button()
            order_number = main_page.get_order_number_from_modal()
            assert order_number
            main_page.click_to_button_close()
            main_page.click_to_order_feed()
            text = order_feed.get_number_order_feed()
            assert order_number in text

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_increases(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов и запомнить текущий счетчик"):
            main_page.click_to_order_feed()
            initial_total = order_feed.get_total_orders_count()
            order_feed.click_to_constructor()
        with allure.step("Добавить булку в заказ и нажать на Войти в аккаунт"):
            main_page.drag_ingredient_to_constructor()
            main_page.click_to_make_order()
        with allure.step("Вход в Личный кабинет"):
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
        with allure.step("Сделать заказ"):
            main_page.click_to_make_order()
            main_page.wait_clickable_close_button()
            main_page.click_to_button_close()
            main_page.click_to_order_feed()
            new_total = order_feed.get_total_orders_count()
            assert new_total > initial_total

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_increases(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Перейти в ленту заказов и запомнить текущий счетчик"):
            main_page.click_to_order_feed()
            initial_total = order_feed.get_today_orders_count()
            order_feed.click_to_constructor()
        with allure.step("Добавить булку в заказ и нажать на Войти в аккаунт"):
            main_page.drag_ingredient_to_constructor()
            main_page.click_to_make_order()
        with allure.step("Вход в Личный кабинет"):
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
        with allure.step("Сделать заказ"):
            main_page.click_to_make_order()
            main_page.wait_clickable_close_button()
            main_page.click_to_button_close()
            main_page.click_to_order_feed()
            new_total = order_feed.get_today_orders_count()
            assert new_total > initial_total

    @allure.title("Номер заказа появляется в разделе «В работе» после оформления")
    def test_order_number_appears_in_work_in_progress(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        order_feed = OrderFeedPage(driver)

        with allure.step("Добавить булку в заказ и нажать на Войти в аккаунт"):
            main_page.drag_ingredient_to_constructor()
            main_page.click_to_make_order()
        with allure.step("Вход в Личный кабинет"):
            login_page.set_email(email)
            login_page.set_password(password)
            login_page.click_to_login()
        with allure.step("Сделать заказ"):
            main_page.click_to_make_order()
            main_page.wait_clickable_close_button()
            order_number = main_page.get_order_number_from_modal()
            assert order_number
            main_page.click_to_button_close()
        with allure.step("Перейти в Ленту заказов"):
            main_page.click_to_order_feed()
            order_feed.wait_visible_text()
            text = order_feed.get_text_in_work()
            assert order_number in text
