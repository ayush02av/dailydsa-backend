from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    PROJECT_TITLE:str = "GDSC Daily Tracker"
    PROJECT_VERSION: str = "1.0.0"

    ACCESS_TOKEN_EXPIRE_MINUTES = 480

    DB_HOSTTYPE = "mysql+mysqlconnector"
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_HOSTNAME = os.getenv('DB_HOSTNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    AUTH_TOKEN_SECRET = os.getenv("AUTH_TOKEN_SECRET")
    AUTH_TOKEN_ALGORITHM = "HS256"

config = Config()