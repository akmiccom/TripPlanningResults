from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# from myLogger import logger

import subprocess
import time

def start_google_chrome_with_port(url):
    
    # logger.info('Start google chrome with port.')
    
    chromePath = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port=9222 --user-data-dir=C:\Temp_Chrome'
    
    subprocess.Popen(chromePath)
    time.sleep(3)

    options = ChromeOptions()
    options.use_chromium = True
    options.debugger_address = r'127.0.0.1:9222'
    
    try:
        chromedriverPath = ChromeDriverManager().install()
        # logger.info('Install chromedriver')
    except:
        chromedriverPath = 'C:\python\chromedriver\chromedriver.exe'
        # logger.info('Submit chromedriver.exe')
    
    service = Service(executable_path=chromedriverPath)
    driver = Chrome(service=service, options=options)
    actionChains = ActionChains(driver)
    
    # これはそれぞれのスクリプトで記述する
    # driver.set_window_position(0, 0)
    # driver.set_window_size(1300, 1000)
    # driver.implicitly_wait(5)
    
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    wait.until(visibility_of_all_elements_located)
    # logger.info('Comleted chromedriver')
    
    return driver, actionChains


def send_keys_and_enter(driver, loginInfo, css):
    
    wait = WebDriverWait(driver, 10)
    wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    if eles:
        eles[0].clear()
        eles[0].send_keys(loginInfo)
        eles[0].send_keys(Keys.ENTER)
        time.sleep(3)
        
    # logger.info('Comleted send_keys_and_enter')
    
def send_keys(driver, loginInfo, css):
    
    wait = WebDriverWait(driver, 10)
    wait.until(visibility_of_all_elements_located((By.CSS_SELECTOR, css)))
    
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    if eles:
        eles[0].clear()
        eles[0].send_keys(loginInfo)
        time.sleep(3)
        
    # logger.info('Comleted send_keys_and_enter')


def sendKeysAtcss(driver, pos=0, inputWord='', sec=3, css=''):
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    eles[pos].clear()
    eles[pos].send_keys(inputWord)
    time.sleep(sec)


def clickAtCss(driver, sec=3, pos=0, css=''):
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    eles[pos].click()
    time.sleep(sec)

if __name__ == '__main__':
    
    driver, actionChains = start_google_chrome_with_port('https://google.com')
    
    driver.quit()
