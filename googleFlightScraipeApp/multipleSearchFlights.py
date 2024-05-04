from setting import FILE_NAME, GOOGLE_FLIGHT_URL, GOOGLE_URL, STOPS, ALLIANCE, SHEET_CLASS, TICKET_TYPE
from setting import createSearchDate
from libs.mySelenium import start_google_chrome_with_port
from libs.myLogger import logger
from searchFlight import searchFlights
from extractFlightInfo import extractFlightInfo
from toCsvFlightInfo import toCsvFlightsInfo
import time
from itertools import product


def getMultipleDates(
    driver,
    departureCodes, arrivalCodes,
    departureDate, beforeDay, arrivalDate, afterDays,
    ticketType, sheetClass, stops, allianceOrairlines
    ):
    
    logger.info('Start multiple date flights informations.')
    
    departureDates = createSearchDate(departureDate, beforeDays=beforeDay, afterDays=afterDays)
    arrivalDates = createSearchDate(arrivalDate, beforeDays=beforeDay, afterDays=afterDays)
    
    dates = list(product(departureDates, arrivalDates))
    codes = list(product(departureCodes, arrivalCodes))
    
    for code, date in list(product(codes, dates)):
        departureCode = code[0]
        arrivalCode = code[1]
        depDate = date[0]
        arrDate = date[1]
    
    # for arrDate in arrivalDates:
    #     for depDate in departureDates:
            
        driver.get(GOOGLE_FLIGHT_URL)
        
        searchFlights(driver, TICKET_TYPE[ticketType], SHEET_CLASS[sheetClass], departureCode, arrivalCode, depDate, arrDate)
        
        extractInfos = extractFlightInfo(driver, stops=STOPS[stops], allianceOrairlines=ALLIANCE[allianceOrairlines])
        
        toCsvFlightsInfo(departureCode, arrivalCode, depDate, arrDate, sheetClass, extractInfos, FILE_NAME)
        
        time.sleep(3)

    logger.info('Completed multiple date flights informations.')
    
    

if __name__ == '__main__':
    
    departureCodes = ['TYO']
    arrivalCodes = ['DPS', 'CGK', 'KUL', 'SIN']

    departureDate = '2024/4/24'
    arrivalDate = '2024/5/1'
    beforeDays, afterDays = 3, 3

    ticketType = 'RoundTrip'
    sheetClass = 'PreEco'
    
    stops = 'OneStop'
    allianceOrairlines = 'StarAlliance'
    allianceOrairlines = 'None'

    driver, actionChains = start_google_chrome_with_port(GOOGLE_URL)

    getMultipleDates(
        driver,
        departureCodes, arrivalCodes,
        departureDate, beforeDays, arrivalDate, afterDays,
        ticketType, sheetClass, stops, allianceOrairlines,
        )