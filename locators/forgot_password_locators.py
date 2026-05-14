from selenium.webdriver.common.by import By


class ForgotPassword:
    input_email_forgot = (
        By.XPATH,
        './/div[@class = "input pr-6 pl-6 input_type_text input_size_default"]',
    )
    input_email_forgot_active = (
        By.XPATH,
        './/input[@class = "text input__textfield text_type_main-default"]',
    )
    button_recover = (
        By.XPATH,
        './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]',
    )
    page_title_reset = (By.XPATH, './/h2[text()="Восстановление пароля"]')
