import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step("Кликнуть на заказ")
    def click_to_order(self):
        self.click(self.locators.order_in_feed)
        self.wait_visible(self.locators.popup_of_order)

    @allure.step("Кликнуть на крестик")
    def click_to_button_close(self):
        self.click(self.locators.button_close)

    @allure.step("Кликнуть на Конструктор")
    def click_to_constructor(self):
        self.click(self.locators.constructor_feed)

    @allure.step("Получить текст из попапа ")
    def get_text_of_popup(self):
        return self.get_text(self.locators.text_in_popup)

    @allure.step("Проверить, что открылось модальное окно")
    def is_modal_window_opened(self):
        try:
            modal = self.find_element(self.locators.popup_of_order)
            return modal.is_displayed()
        except:
            return False

    @allure.step("Получить общее количество выполненных заказов ")
    def get_total_orders_count(self):
        return self.get_text(self.locators.text_order_feed_number)

    @allure.step("Получить общее количество выполненных заказов ")
    def get_today_orders_count(self):
        return self.get_text(self.locators.text_order_feed_number_today)

    @allure.step("Получить номера заказов в работе")
    def get_text_in_work(self):
        return self.get_text(self.locators.place_in_work)

    @allure.step("Получить номера заказов в Ленте")
    def get_number_order_feed(self):
        return self.get_text(self.locators.number_order_in_feed)

    @allure.step("Подождать появления заказа в ленте")
    def wait_number_order(self):
        self.wait_visible(self.locators.number_order_in_work)

    @allure.step("Подождать появления заказа в ленте")
    def wait_invisible_text(self):
        self.wait_invisible(self.locators.text_all_order_ready)
