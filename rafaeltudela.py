
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.saucedemo.com/")
    
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    
    assert "inventory.html" in driver.current_url
    print("Teste SauceDemo: Login com sucesso!")

except Exception as e:
    print(f"Teste SauceDemo: Falhou - {e}")

finally:
    time.sleep(3)
    driver.quit()



    

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    success_message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in success_message
    print("Teste Herokuapp: Login com sucesso!")

except Exception as e:
    print(f"Teste Herokuapp: Falhou - {e}")

finally:
    time.sleep(3)
    driver.quit()




service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    success_message = driver.find_element(By.CLASS_NAME, "post-title").text
    assert "Logged In Successfully" in success_message
    print("Teste Practice Test Automation: Login com sucesso!")

except Exception as e:
    print(f"Teste Practice Test Automation: Falhou - {e}")

finally:
    time.sleep(3)
    driver.quit()




service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    time.sleep(2) 

    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    
    time.sleep(5)
    
    assert "dashboard" in driver.current_url
    print("Teste OrangeHRM: Login com sucesso!")

except Exception as e:
    print(f"Teste OrangeHRM: Falhou - {e}")

finally:
    time.sleep(3)
    driver.quit()