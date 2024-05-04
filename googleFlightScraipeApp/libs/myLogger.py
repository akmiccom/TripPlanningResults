from logging import getLogger, basicConfig, StreamHandler, Formatter, FileHandler, INFO, DEBUG, ERROR, WARNING
import datetime
import os
import pathlib

today = datetime.date.today().strftime('%Y-%m-%d')


# log ディレクトリの作成
BASE_DIR = pathlib.Path(__file__).parents[2]
logDir = f'{BASE_DIR}/log'
if not os.path.exists(logDir):
    os.mkdir(logDir)

# create logger
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# create console handler and set level to debug

# 標準出力
handler = StreamHandler()
handler.setLevel(INFO)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# DEBUGファイル出力
debugHandler = FileHandler(f'log/Debug_{today}.log', encoding='utf-8')
debugHandler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
debugHandler.setFormatter(formatter)
logger.addHandler(debugHandler)

# INFOファイル出力
infoHandler = FileHandler(f'log/Information_{today}.log', encoding='utf-8')
infoHandler.setLevel(INFO)
formatter = Formatter('%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
infoHandler.setFormatter(formatter)
logger.addHandler(infoHandler)

