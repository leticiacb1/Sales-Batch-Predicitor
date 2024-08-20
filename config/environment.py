import os
from os.path import join, dirname, abspath
from dotenv import load_dotenv

class EnvironmentVariables():

    def __init__(self) -> None:
        self.dotenv_path = join(dirname(abspath(__file__)), '.env')
        
        self.HOST = None
        self.PORT = None
        self.USERNAME = None
        self.PASSWORD = None
        self.DATABASE = None
        self.GITHUB_TOKEN = None

    def get(self) -> None:

        # Reading .env and creating environment variables
        load_dotenv(self.dotenv_path)

        # Reading environment variable
        self.HOST = os.getenv("DB_HOST")
        self.PORT = os.getenv("DB_PORT")
        self.USERNAME = os.getenv("DB_USER")
        self.PASSWORD = os.getenv("DB_PASSWORD")
        self.DATABASE = os.getenv("DB_DATABASE")
        self.GITHUB_TOKEN = os.getenv("GITHUB_TOKEN_ACCESS")