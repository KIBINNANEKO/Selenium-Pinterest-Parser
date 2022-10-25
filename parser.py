from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import fake_useragent
from tok import path, password1, email1

import random, time, os

ua = fake_useragent.UserAgent()

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={ua}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(executable_path= fr"{path}", options=options)
action = ActionChains(driver)

def autorisation(url):
    driver.get(url=url)
    time.sleep(2)
    driver.find_element(By.XPATH, '//div[@data-test-id="simple-login-button"]').click()
    time.sleep(2)
    email = driver.find_element(By.ID, 'email')
    email.clear()
    email.send_keys(email1)
    time.sleep(1)
    password = driver.find_element(By.ID, 'password')
    password.clear()
    password.send_keys(password1)
    time.sleep(3)
    driver.find_element(By.XPATH, '//div[@data-test-id="registerFormSubmitButton"]').click()
    time.sleep(3)

def exit():
    driver.close()
    driver.quit()

def downloading(index, quantity):
    i = 0
    while quantity != index:
        if quantity == 12:
            driver.refresh()
            i = 0
            time.sleep(3)
        items = driver.find_elements(By.XPATH, '//div[@data-test-id="non-story-pin-image"]')
        items[i].click()
        time.sleep(3)
        try:
            other = driver.find_element(By.XPATH, '//button[@aria-label="Другие варианты"]')
            action.move_to_element(other)
            time.sleep(0.5)
            other.click()
            time.sleep(0.2)
            driver.find_element(By.ID, "pin-action-dropdown-item-0").click()
            time.sleep(0.3)
            driver.back()
            time.sleep(1)
            quantity += 1
            i += 1
        except:
            driver.refresh()
            downloading(index, quantity)
            quantity += 1

    print('Все файлы успешно загрузились, до свидания!')
    exit()

# доработать
#def naming_moving():
#    all_downloads = os.listdir(path=r"C:\Users\KIBINNANEKO\Downloads")
#    downloads = set(all_downloads)

#    for i in downloads:
#       name = f"random aestetic pic №{random.randint(0, 10000000)}.jpg"
#        os.replace(fr"C:\Users\KIBINNANEKO\Downloads\{i}",
#                   fr"C:\Users\KIBINNANEKO\PycharmProjects\Parser Pinterest\Pins\{name}")
