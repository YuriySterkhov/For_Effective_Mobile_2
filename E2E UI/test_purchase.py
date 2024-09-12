import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_purchase():    
    def send_keys_with_delays(element, value):
        wait = WebDriverWait(driver, 10)
        for i in range(len(value)):
            element.send_keys(value[i])
            wait.until(lambda _: element.get_property('value')[:i] == value[:i])


    # Настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        wait = WebDriverWait(driver, 10)
        # 1. Переход на сайт
        driver.get("https://www.saucedemo.com")
        
        # 2. Авторизация
        # закомментированные строки кода:
        # element = ...
        # element.click
        # являются альтернативой строке кода над ними для случая,
        # когда необходима задержка между поиском элемента на странице
        # и имитацией клика мышью по найденному элементу;
        # у меня была проблема с обоими вариантами до исправления неверного
        # селектора (вариант с задержкой был поиском решения проблемы);
        # после исправления селектора оба варианта работают

        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        send_keys_with_delays(driver.find_element(By.ID, "user-name"), "standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        send_keys_with_delays(driver.find_element(By.ID, "password"), "secret_sauce")
        # driver.find_element(By.ID, "login-button").click()
        element = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
        element.click()
        
        # 3. Выбор товара
        driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        # element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")))
        # element.click()
        
        # 4. Переход в корзину
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        # element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']")))
        # element.click()
        
        # 5. Проверка, что товар добавлен в корзину
        assert driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']") is not None
        
        # 6. Оформление покупки
        driver.find_element(By.ID, "checkout").click()
        # driver.find_element(By.ID, "first-name").send_keys("John")
        send_keys_with_delays(driver.find_element(By.ID, "first-name"), "John")
        # driver.find_element(By.ID, "last-name").send_keys("Doe")
        send_keys_with_delays(driver.find_element(By.ID, "last-name"), "Doe")
        # driver.find_element(By.ID, "postal-code").send_keys("12345")
        send_keys_with_delays(driver.find_element(By.ID, "postal-code"), "12345")
        driver.find_element(By.ID, "continue").click()
        # element = wait.until(EC.presence_of_element_located((By.ID, "continue")))
        # element.click()
        driver.find_element(By.ID, "finish").click()
        # element = wait.until(EC.presence_of_element_located((By.ID, "finish")))
        # element.click()
        
        # 7. Проверка успешного завершения покупки
        assert driver.find_element(By.XPATH, "//h2[text()='THANK YOU FOR YOUR ORDER']") is not None
        
    finally:
        # 8. Закрыть браузер
        time.sleep(3)  # Для просмотра завершения теста
        driver.quit()

if __name__ == "__main__":
    test_purchase()
