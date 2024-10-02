import os
from dotenv import load_dotenv # библиатека для чтения переменных среды из файла .env

load_dotenv() # ищет и подгружает переменные из файла .env

class Config(): # клас для удобного обращения к конфигурационным переменным

    api_id = os.getenv('TELEGRAM_API_ID')
    api_hash = os.getenv('TELEGRAM_API_HASH')
    phone_num = os.getenv('PHONE_NUM')
    session_name = 'session' # файл сессии в котором хранянится информация для автоматического входа