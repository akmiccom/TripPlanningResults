from setting import FILE_NAME, EXCEL_FILE_NAME, GOOGLE_FLIGHT_URL, GOOGLE_URL, STOPS, ALLIANCE, SHEET_CLASS, TICKET_TYPE
from libs.mySelenium import start_google_chrome_with_port
from libs.myDatetime import now
from libs.myLogger import logger
from searchFlight import searchFlights
from extractFlightInfo import extractFlightInfo

import re
import os
import pandas as pd

    
def toCsvFlightsInfo(departureCode, arrivalCode, departureDate, arrivalDate, sheetClass, extractInfos, fileName):
    
    logger.info('Start edit flights informations.')
    
    editInfos = [[i for i in re.split(r'。 ', info) if not re.search(r'選択', i)] for info in extractInfos]
    for editInfo in editInfos:
        editInfo.insert(0, now.strftime('%Y/%m/%d'))
    
    # Edit information
    df = pd.DataFrame(editInfos)
    pdDatetime = df.iloc[:, 0]
    departureDates = pd.Series([departureDate for _ in range(len(df.iloc[:, 0]))])
    arrivalDates = pd.Series([arrivalDate for _ in range(len(df.iloc[:, 0]))])
    departureCodes = pd.Series([departureCode for _ in range(len(df.iloc[:, 0]))])
    arrivalCodes = pd.Series([arrivalCode for _ in range(len(df.iloc[:, 0]))])
    sheetClass = pd.Series([sheetClass for _ in range(len(df.iloc[:, 0]))])
    price = df.iloc[:, 1].str.replace(r'[\u3400-\u9FFF\uF900-\uFAFF]|[の ～]', '', regex=True).astype(int)
    airline = df.iloc[:, 2].str.replace(r'が運航する|のフライト', ' ', regex=True).str.split(r'経由地|直行便', expand=True)
    schedule = df.iloc[:, 3].str.split(r'曜日, |月 |、|(?<=[0-9]{2} )|(?<=発)', expand=True)  # 正規表現で修正
    totalTime = df.iloc[:, 4].str.replace(r'合計時間', '', regex=True)
    transit1 = df.iloc[:, 5].str.replace(r'乗り継ぎ（|）は、|における |です|の| ', ' ', regex=True)
    # 経由地２か所未対応
    # transit2 = df.iloc[:, 6].str.replace(r'乗り継ぎ（|）は、|における |です|の| ', ' ', regex=True)
    

    flightInfos = pd.concat([
        pdDatetime, departureDates, arrivalDates, departureCodes, arrivalCodes, sheetClass, price, airline, totalTime, schedule, transit1
        ], axis=1)
    
    columns = [
        'GetTime', 'DepDate', 'ArrDate', 'Dep', 'Arr',
        'Sheet', 'Price', 'Airline', 'Via ', 'TotalTime',
        'd_W', 'd_M', 'd_D', 'd_Time', 'd_Airport',
        'a_W', 'a_M', 'a_D', 'a_Time', 'a_Airport',
        'Via place',
        ]
    flightInfos.columns = columns
    
    if os.path.exists(fileName):
        flightInfos.to_csv(fileName, mode='a', index=False, header=False, encoding='shift-jis')
    else:
        flightInfos.to_csv(fileName, mode='w', index=False, encoding='shift-jis')
    
    logger.info('Completed edit flights informations.')
    
def csvToExcel():
    
    csv = pd.read_csv(FILE_NAME, encoding='shift-jis')
    csv.drop_duplicates(inplace=True)
    csv.to_excel(EXCEL_FILE_NAME, index=False)





if __name__ == '__main__':
    
    departureCode = 'SIN'
    arrivalCode = 'JFK'
    
    departureDate = '2024/4/24'
    arrivalDate = '2024/5/1'
    
    ticketType = 'RoundTrip'
    sheetClass = 'PreEco'
    
    stops = 'OneStop'
    allianceOrairlines = 'StarAlliance'
    allianceOrairlines = 'None'
    
    driver, actionChains = start_google_chrome_with_port(GOOGLE_URL)
    
    driver.get(GOOGLE_FLIGHT_URL)
    
    searchFlights(driver, TICKET_TYPE[ticketType], SHEET_CLASS[sheetClass], departureCode, arrivalCode, departureDate, arrivalDate)
    
    extractInfos = extractFlightInfo(driver, stops=STOPS[stops], allianceOrairlines=ALLIANCE[allianceOrairlines])

    toCsvFlightsInfo(departureCode, arrivalCode, departureDate, arrivalDate, sheetClass, extractInfos, FILE_NAME)
    
    csvToExcel()