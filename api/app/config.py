import os


class Config:
    BROKER_URL = os.getenv('BROKER_URL')
