from setting import GOOGLE_FLIGHT_URL, GOOGLE_URL, SHEET_CLASS, TICKET_TYPE, STOPS, ALLIANCE
from libs.mySelenium import start_google_chrome_with_port, sendKeysAtcss, clickAtCss
from libs.myLogger import logger
import time


def searchFlights(driver, ticketType, sheetClass, departureCode, arrivalCode, departureDate, arrivalDate):
    
    logger.info('Start search flights.')
    
    # Round trip, One way, Multiple city
    clickAtCss(driver, pos=ticketType, css='c-wiz > div > div > div > div > div > div > div')
    clickAtCss(driver, pos=0, css='c-wiz > div > div > div > div > div > div > div > div > div > div > div > ul > li')

    # Class 3: Economy, 4: PreEco, 5: Bussines, 6: First
    clickAtCss(driver, pos=2, css='c-wiz > div > div > div > div > div > div > div')
    clickAtCss(driver, pos=sheetClass, css='c-wiz > div > div > div > div > div > div > div > div > div > div > div > ul > li')

    # Deperture
    sendKeysAtcss(driver, inputWord=departureCode, css='div > div.cQnuXe.k0gFV > div > div > input')
    clickAtCss(driver, css='ul > li > div > div > div')
    clickAtCss(driver, css='c-wiz > div > c-wiz > div > div > div')

    # Arrival
    sendKeysAtcss(driver, pos=1, inputWord=arrivalCode, css='div > div.cQnuXe.k0gFV > div > div > input')
    clickAtCss(driver, css='ul > li > div > div > div')
    clickAtCss(driver, css='c-wiz > div > c-wiz > div > div > div')

    # Deperture date
    sendKeysAtcss(driver, inputWord=departureDate, css='div > div.cQnuXe.k0gFV > div > div > div > div > div > div > input')
    clickAtCss(driver, sec=1, css='c-wiz > div > c-wiz > div > div > div')

    # Arraival date
    sendKeysAtcss(driver, pos=1, inputWord=arrivalDate, css='div > div.cQnuXe.k0gFV > div > div > div > div > div > div > input')
    clickAtCss(driver, sec=1, css='c-wiz > div > c-wiz > div > div > div')

    # Click search
    clickAtCss(driver, css='c-wiz > div > div > div > div > div > button > span')
    
    logger.info('Completed search flights.')
    

if __name__ == '__main__':
    
    logger.info('Start google Flights App.')
    
    departureCode = 'SIN'
    arrivalCode = 'JFK'
    
    departureDate = '2024/4/24'
    arrivalDate = '2024/5/1'
    
    ticketType = 'RoundTrip'
    sheetClass = 'PreEco'
    
    stops = 'OneStop'
    allianceOrairlines = 'StarAlliance'
    
    settings = [
        departureCode, arrivalCode, departureDate, arrivalDate,
        ticketType, sheetClass, stops, allianceOrairlines,
        ]
    for setting in settings:
        logger.info(f'[{setting}] selected.')
        # time.sleep(0.2)
    
    driver, actionChains = start_google_chrome_with_port(GOOGLE_URL)
    
    driver.get(GOOGLE_FLIGHT_URL)
    
    searchFlights(driver, TICKET_TYPE[ticketType], SHEET_CLASS[sheetClass], departureCode, arrivalCode, departureDate, arrivalDate)