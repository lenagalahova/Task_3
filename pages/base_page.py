import allure
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Найти элемент ")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти видимый элемент")
    def find_element_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст в поле")
    def send_keys(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Получить текст из элемента")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ожидать видимость элемента")
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидать кликабельности")
    def clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать невидимость элемента")
    def wait_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Скроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
