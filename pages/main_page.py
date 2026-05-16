import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Кликнуть на кнопку 'Личный кабинет'")
    def click_to_lk_button(self):
        self.clickable(self.locators.lk_button)
        self.click(self.locators.lk_button)

    @allure.step("Кликнуть на кнопку 'Конструктор'")
    def click_to_constructor(self):
        self.click(self.locators.constructor)

    @allure.step("Кликнуть на кнопку 'Лента заказов'")
    def click_to_order_feed(self):
        self.click(self.locators.order_feed)
        self.wait_invisible(self.locators.constructor_place)

    @allure.step("Получить заголовок Соберите бургер")
    def get_title_of_page(self):
        return self.get_text(self.locators.title_constructor_page)

    @allure.step("Кликнуть на 'Флюоресцентная булка'")
    def click_to_bun(self):
        self.click(self.locators.bun)
        self.wait_visible(self.locators.popap_ingredient)

    @allure.step("Получить заголовок Детали ингредиента")
    def get_title_of_popup(self):
        return self.get_text(self.locators.popap_ingredient)

    @allure.step("Проверить невидимость попапа")
    def is_invisibility_popap(self):
        try:
            self.wait_invisible(self.locators.popap_ingredient)
            return True
        except TimeoutError:
            return False

    @allure.step("Перетаскиваем ингредиент в зону 'Выбранные ингредиенты'")
    def drag_ingredient_to_constructor(self):
        ingredient = self.find_element(self.locators.bun)
        constructor_area = self.find_element(self.locators.constructor_place)

        ActionChains(self.driver).drag_and_drop(ingredient, constructor_area).perform()

    @allure.step("Проверить, что булка добавилась в конструктор")
    def is_bun_in_constructor(self):
        try:
            # Проверяем верхнюю булку
            bun_top = self.find_element(self.locators.souse)
            return bun_top.is_displayed()
        except:
            return False

    @allure.step("Получить текст каунтера")
    def get_text_counter(self):
        return self.get_text(self.locators.button_count)

    @allure.step("Кликнуть на кнопку 'Сделать заказ'")
    def click_to_make_order(self):
        self.click(self.locators.button_make_order)

    @allure.step("Подождать кликабельности крестика")
    def wait_clickable_close_button(self):
        self.clickable(self.locators.button_close_making_order)

    @allure.step("Кликнуть крестик")
    def click_to_button_close(self):
        self.clickable(self.locators.button_close)
        self.click(self.locators.button_close)
        self.wait_invisible(self.locators.text_start_cooking)

    @allure.step("Получить заголовок Ваш заказ начали готовить")
    def get_text_of_starting_make_order(self):
        return self.get_text(self.locators.text_start_cooking)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text(self.locators.order_number_modal_title)
