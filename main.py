import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def run():
    driver.get("https://www.speedtest.net/")

    add = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div/div/div[3]/button')
    add.click()

    go_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]')
    go_button.click()

    intr = driver.find_element(By.XPATH,
                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
    ms = driver.find_element(By.XPATH,
                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

    time.sleep(40)

    speed = f"my internet internet speed  is {intr.text} and my ms is {ms.text} "
    print(speed)

    driver.close()
    return speed


run()
