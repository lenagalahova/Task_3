import allure
from locators.lk_locator import LKPageLocators
from pages.base_page import BasePage


class LKPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LKPageLocators()

    @allure.step("Кликнуть на кнопку 'История заказов'")
    def click_to_history(self):
        self.wait_visible(self.locators.button_history)
        self.click(self.locators.button_history)

    @allure.step("Кликнуть на кнопку 'Выход'")
    def click_to_logout(self):
        self.clickable(self.locators.button_logout)
        self.click(self.locators.button_logout)

    @allure.step("Получить текст История заказов на странице")
    def get_title_of_page(self):
        return self.get_text(self.locators.button_history)
