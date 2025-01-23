from selenium.webdriver.common.by import By
    
'''
Проверяем, что кнопка добавления в корзину на месте
'''
def test_add_to_cart_button_presence(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    add_to_cart_btn = browser.find_element(By.XPATH, "//button[@type='submit']")
    
    assert add_to_cart_btn is not None