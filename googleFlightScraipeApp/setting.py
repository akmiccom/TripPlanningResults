import pathlib
from datetime import datetime, date, timedelta


def createSearchDate(inputDate, beforeDays, afterDays):
    
    centerDate = datetime.strptime(inputDate, '%Y/%m/%d')
    createDates = [(centerDate + timedelta(days=n)).strftime('%Y/%m/%d') for n in range(-beforeDays, afterDays+1, 1)]
    
    return createDates



ROOT_DIR = pathlib.Path(__file__).parents[1]

FILE_NAME = f'{ROOT_DIR}/csv/searchResults.csv'
EXCEL_FILE_NAME = f'{ROOT_DIR}/csv/searchResults.xlsx'

GOOGLE_FLIGHT_URL = 'https://www.google.com/travel/flights?hl=ja'

GOOGLE_URL = 'https://google.com'

TICKET_TYPE = {
    'RoundTrip': 0,
    'Round Trip': 0,
    'OneWay': 1,
    'One Way': 1,
    'MultipleCity': 2,
    'Multiple City': 2,
    }

SHEET_CLASS = {
    'Economy': 3,
    'PreEco': 4,
    'Bussines': 5,
    'First': 6,
    }

STOPS = {
    'AnyStops': 0,
    'Any Stops': 0,
    'Direct': 1,
    'OneStop': 2,
    'One Stop': 2,
    'TwoStop': 3,
    'Two Stop': 3,
    }

ALLIANCE = {
    'StarAlliance': 0,
    'Star Alliance': 0,
    'SkyTeam': 1,
    'Sky Team': 1,
    'Oneworld': 2,
    'One world': 2,
    'None': 99,
    }

AIRLINES = {
    'ANA': 0,
    'Bamboo Airways': 1,
    'JAL': 2,
    'MIAT モンゴル航空': 3,
    'Peach': 4,
    'STARLUX': 5,
    'THAI': 6,
    'ZIPAIR Tokyo': 7,
    'アシアナ航空': 8,
    'ヴァージン・オーストラリア': 9,
    'ヴィスタラ': 10,
    'ウエストジェット航空': 11,
    'エア インディア': 12,
    'エアアジア': 13,
    'エアアジア・フィリピン': 14,
    'エアアジアX': 15,
    'エチオピア航空': 16,
    'エバー航空': 17,
    'カタール航空': 18,
    'ガルーダ・インドネシア航空': 19,
    'キャセイパシフィック航空': 20,
    'ジェットスター': 21,
    'ジェットスター・アジア航空': 22,
    'シンガポール航空': 23,
    'スカイマーク': 24,
    'スクート': 25,
    'スターフライヤー': 26,
    'スリランカ航空': 27,
    'セブパシフィック航空': 28,
    'タイ・エアアジア': 29,
    'タイ・ベトジェット・エア': 30,
    'タイ・ライオン・エア': 31,
    'チェジュ航空': 32,
    'チャイナ エアライン': 33,
    'ティーウェイ航空': 34,
    'ニュージーランド航空': 35,
    'ハワイアン航空': 36,
    'バンコク・エアウェイズ': 37,
    'ビーマン・バングラデシュ航空': 38,
    'フィリピン航空': 39,
    'フレックスフライト': 40,
    'ベトジェット・エア': 41,
    'ベトナム航空': 42,
    'マカオ航空': 43,
    'マリンド・エア': 44,
    'マレーシア航空': 45,
    'ルフトハンザドイツ航空': 46,
    'ロイヤルブルネイ航空': 47,
    '吉祥航空': 48,
    '四川航空': 49,
    '春秋航空': 50,
    '上海航空': 51,
    '深圳航空': 52,
    '大韓航空': 53,
    '中国国際航空': 54,
    '中国東方航空': 55,
    '中国南方航空': 56,
    '厦門航空': 57,
    }