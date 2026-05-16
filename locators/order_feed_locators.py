from selenium.webdriver.common.by import By


class OrderFeedLocators:
    constructor_feed = (
        By.XPATH,
        './/p[@class = "AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]',
    )
    # Выполнено за все время:
    text_order_feed_number = (
        By.XPATH,
        './/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]',
    )
    # Выполнено за сегодня:
    text_order_feed_number_today = (
        By.XPATH,
        './/p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"]',
    )
    place_in_work = (
        By.XPATH,
        './/ul[@class = "OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]',
    )
    number_order_in_work = (
        By.XPATH,
        './/li[@class = "text text_type_digits-default mb-2"]',
    )
    number_order_in_feed = (By.XPATH, './/p[@class = "text text_type_digits-default"]')
    text_order_in_work = (
        By.XPATH,
        './/ul[contains(@class, "OrderFeed_orderListReady")]//li[contains(@class, "text_type_digits-default")]',
    )
    order_in_feed = (By.XPATH, '//ul[contains(@class, "OrderFeed")]//li[1]')
    popup_of_order = (
        By.XPATH,
        './/div[@class = "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]',
    )
    text_in_popup = (By.XPATH, './/h2[text()="Состав"]')

    button_close = (
        By.XPATH,
        './/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]',
    )
