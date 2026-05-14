from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    password_input = (By.XPATH, './/input[@type="password"]')
    code_input = (By.XPATH, './/input[@type="text"]')
    button_save = (By.XPATH, './/button[text()="Сохранить"]')
    eye_icon = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    # active_input= (By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    active_input = (By.XPATH, './/div[contains(@class, "input_status_active")]')
