from setting import FILE_NAME, GOOGLE_FLIGHT_URL, GOOGLE_URL, STOPS, ALLIANCE, TICKET_TYPE, SHEET_CLASS, ROOT_DIR
from libs.myDatetime import now, today
from libs.mySelenium import start_google_chrome_with_port, clickAtCss
from libs.myLogger import logger
from searchFlight import searchFlights

from selenium.webdriver.common.by import By
import time
import csv



urls = {
    'ana': 'https://www.google.com/travel/explore?tfs=CBwQAxosEgoyMDI0LTA1LTEwMgJOSGoMCAMSCC9tLzA3ZGZrcgwIBBIIL20vMDJqNzEaLBIKMjAyNC0wNS0xNjICTkhqDAgEEggvbS8wMmo3MXIMCAMSCC9tLzA3ZGZrQAFIAXACggELCP___________wGYAQGyAQQYASAB&tfu=GgA&hl=en-GB',
    'star': 'https://www.google.com/travel/explore?tfs=CBwQAxo3EgoyMDI0LTEwLTE3Mg1TVEFSX0FMTElBTkNFagwIAxIIL20vMDdkZmtyDAgEEggvbS8wMmo3MRo3EgoyMDI0LTEwLTIzMg1TVEFSX0FMTElBTkNFagwIBBIIL20vMDJqNzFyDAgDEggvbS8wN2Rma0ABSAFwAYIBCwj___________8BmAEBsgEEGAEgAQ&tfu=GgA&hl=en-GB',
    'all': 'https://www.google.com/travel/explore?tfs=CBwQAxooEgoyMDI0LTEwLTE3agwIAxIIL20vMDdkZmtyDAgEEggvbS8wMmo3MRooEgoyMDI0LTEwLTIzagwIBBIIL20vMDJqNzFyDAgDEggvbS8wN2Rma0ABSAFwAYIBCwj___________8BmAEBsgEEGAEgAQ&tfu=GioaKAoSCcSqy5dDD1RAEQAAAAAAgGZAEhIJOlY_fXHaUcARAAAAAACAZsA&hl=en-GB',
}

period = {
    'weekend': 0,
    '1week': 1,
    '2weeks': 2,
}

dates = {
    'allMonth': 0,
    'thisMonth': 1,
    'nextMonth': 2,
    '2MonthsLater': 3,
    '3MonthsLater': 4,
    '4MonthsLater': 5,
    '5MonthsLater': 6,
}


def input_departure(SEC, departure, driver):
# 出発地入力
## 入力
    css = 'section > div > div > div > div > div > div > div > div > div > div > div > div > input'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
# for i, ele in enumerate(eles):
#     print(i, ele.text.replace('\n', ' '))
    eles[0].clear()
    eles[0].send_keys(departure)
    print(eles[0].text.replace('\n', ' '))
    time.sleep(SEC)

## 選択
    css = 'section > div > div > div > div > div'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    for i, ele in enumerate(eles):
        if departure in ele.text:
            print(i, ele.text.replace('\n', ' '))
            ele.click()
    time.sleep(5)


def period_input(SEC, period, dates, driver):
# 検索期間入力
## 選択
    css = 'section > div > div > div > div > div > div > div > div > div > div > div > div > div > div'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    for i, ele in enumerate(eles):
        if 'week' in ele.text:
            print(i, ele.text.replace('\n', ' '))
            ele.click()
    time.sleep(SEC)

## 検索月選択
    css = 'span > div > div > div:nth-child(1) > span > span > span > button > span'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    for i, ele in enumerate(eles):
    # if 'June' in ele.text:
        print(i, ele.text.replace('\n', ' '))
    # eles[dates['thisMonth']].click()
    eles[dates].click()
    time.sleep(SEC)

## 検索期間選択
    css = 'span > div > div > div:nth-child(2) > span > span > span > button > span'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    for i, ele in enumerate(eles):
    # if '1 week' in ele.text:
        print(i, ele.text.replace('\n', ' '))
    # eles[period['1week']].click()
    eles[period].click()
    time.sleep(SEC)

## 実行クリック
    css = 'div > div > div > div > button'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    for i, ele in enumerate(eles):
        if 'Done' in ele.text:
            print(i, ele.text.replace('\n', ' '))
            ele.click()
    time.sleep(5)


def extract_information(SEC, departure, driver):
# csv保存
## 情報抽出
    css = 'main > div > div > div > ol > li > div > div'
    eles = driver.find_elements(By.CSS_SELECTOR, css)
    infos = []
    for i, ele in enumerate(eles):
        if ele.text != '':
            print(i, end=', ')
            infos.append([departure] + ele.text.split('\n'))
            time.sleep(0.5)
    print()
    return infos


def to_csv(departure, infos, mode):
## 保存
    with open(f'{departure}', mode, encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(infos)
    print('Finished extract')


departure = 'GMP'
departure = 'SYD'
departure = 'LHR'
departure = 'JFK'
departure = 'SIN'
departure = 'KUL'
departure = 'CGK'
departure = 'HKG'
departure = 'TPE'

departures = ['HND', 'NRT', 'HKG', 'TPE', 'CGK', 'SYD', 'GMP', 'SIN', 'KUL']

SEC = 2

if __name__ == '__main__':

    driver, actionChains = start_google_chrome_with_port(GOOGLE_URL)
    
    driver.get(urls['ana'])

    for i, (k, v) in enumerate(dates.items()):

        # period_input(SEC, period['1week'], dates['allMonth'], driver)
        period_input(SEC, period['1week'], dates[k], driver)

        for j, departure in enumerate(departures):

            input_departure(SEC, departure, driver)
            infos = extract_information(SEC, departure, driver)
            to_csv(FILE_NAME, infos, 'a')
            print(f'The {j+1} session has ended.')
    print(f'All session has ended.')

    driver.quit()