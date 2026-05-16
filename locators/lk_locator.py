from selenium.webdriver.common.by import By


class LKPageLocators:
    button_history = (
        By.XPATH,
        './/a[@class = "Account_link__2ETsJ text text_type_main-medium text_color_inactive" and text()="История заказов"]',
    )
    button_logout = (
        By.XPATH,
        './/button[@class = "Account_button__14Yp3 text text_type_main-medium text_color_inactive" and text()="Выход"]',
    )
    order_history = (
        By.XPATH,
        './/div[@class = "OrderHistory_orderHistory__qy1VB"]',
    )
