from setting import GOOGLE_FLIGHT_URL, GOOGLE_URL, STOPS, ALLIANCE, TICKET_TYPE, SHEET_CLASS, ROOT_DIR
from libs.myDatetime import now, today
from libs.mySelenium import start_google_chrome_with_port, clickAtCss
from libs.myLogger import logger
from searchFlight import searchFlights

from selenium.webdriver.common.by import By


def extractFlightInfo(driver, stops, allianceOrairlines):
    
    logger.info('Start extract flights infomation.')
    
    # Number of transit pos=1 : Direct, pos=2 : one transit, pos=3 : two transit
    clickAtCss(driver, css='div > span > button > span > span > span')
    clickAtCss(driver, pos=stops, css='c-wiz > div > div > c-wiz > div > c-wiz > div > div > div > div > div > div > div > div > div > section > div > div > div > div > div > label')
    clickAtCss(driver, pos=1, css='c-wiz > div > c-wiz > div > div > div > div > div > div > span')
    
    # Select alliance pos=0 : Star
    if allianceOrairlines == 99:
        logger.info('Not selected an airline or alliance.')
    elif allianceOrairlines in [0, 1, 2]:
        clickAtCss(driver, css='div > span > button > span > span > span')
        # clickAtCss(driver, pos=allianceOrairlines, css='c-wiz > div > c-wiz > div > div > div > div > div > div > div > div > div > section > div > div > div > div > div > div > div > div > ol > li > label')
        clickAtCss(driver, pos=allianceOrairlines, css='section > div > div > div > div > div > div > div > div > ol > li > label')
        clickAtCss(driver, pos=1, css='c-wiz > div > c-wiz > div > div > div > div > div > div > span')
        
    
    # Extract infomation
    eles = driver.find_elements(By.CSS_SELECTOR, 'c-wiz > div > div > div > ul > li > div > div')
    extractInfos = [ele.get_attribute('aria-label') for ele in eles if ele.get_attribute('aria-label') != None]
    
    # add text
    with open(f'{ROOT_DIR}/csv/searchResults.txt', 'a', encoding='utf-8') as f:
        for i, extractInfo in enumerate(extractInfos):
            f.write(f'{now} - {extractInfo}\n')
    
    logger.info('Completed extract flights infomation.')
    
    return extractInfos


if __name__ == '__main__':
    
    departureCode = 'SIN'
    arrivalCode = 'JFK'
    
    departureDate = '2024/8/1'
    arrivalDate = '2024/9/1'
    
    ticketType = 'RoundTrip'
    sheetClass = 'PreEco'
    
    stops = 'OneStop'
    allianceOrairlines = 'None'
    # allianceOrairlines = 'StarAlliance'
    
    driver, actionChains = start_google_chrome_with_port(GOOGLE_URL)
    
    driver.get(GOOGLE_FLIGHT_URL)
    
    searchFlights(driver, TICKET_TYPE[ticketType], SHEET_CLASS[sheetClass], departureCode, arrivalCode, departureDate, arrivalDate)
    
    extractInfos = extractFlightInfo(driver, stops=STOPS[stops], allianceOrairlines=ALLIANCE[allianceOrairlines])