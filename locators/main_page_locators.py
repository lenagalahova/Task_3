from selenium.webdriver.common.by import By


class MainPageLocators:
    lk_button = (
        By.XPATH,
        './/p[@class = "AppHeader_header__linkText__3q_va ml-2" and text()="Личный Кабинет"]',
    )
    constructor = (
        By.XPATH,
        './/p[@class = "AppHeader_header__linkText__3q_va ml-2" and text()="Конструктор"]',
    )
    order_feed = (By.XPATH, './/p[text()="Лента Заказов"]')
    title_constructor_page = (By.XPATH, './/h1[text()="Соберите бургер"]')

    bun = (
        By.XPATH,
        "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and .//p[text()='Флюоресцентная булка R2-D3']]",
    )
    souse = (
        By.XPATH,
        ".//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6') and .//p[text()='Соус Spicy-X']]",
    )
    constructor_place = (
        By.XPATH,
        ".//section[contains(@class, 'BurgerConstructor_basket__29Cd7 mt-25 ')]",
    )
    popap_ingredient = (
        By.XPATH,
        './/h2[@class = "Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10" and text()="Детали ингредиента"]',
    )
    button_close = (
        By.XPATH,
        './/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]',
    )
    button_count = (
        By.XPATH,
        "//p[text()='Флюоресцентная булка R2-D3']/ancestor::a//p[contains(@class,'counter_counter__num')]",
    )
    button_count_souse = (
        By.XPATH,
        "//p[text()='Соус Spicy-X']/ancestor::a//p[contains(@class,'counter_counter__num')]",
    )
    button_make_order = (
        By.XPATH,
        './/button[@class = "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]',
    )
    order_number_modal_title = (
        By.XPATH,
        './/h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]',
    )

    text_start_cooking = (
        By.XPATH,
        './/p[@class = "undefined text text_type_main-small mb-2"]',
    )
    button_close_making_order = (
        By.XPATH,
        './/button[@class = "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]',
    )
