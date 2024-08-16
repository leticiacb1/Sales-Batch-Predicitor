import os
from os.path import join, dirname
from dotenv import load_dotenv

# Reading .env and creating environment variables
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# Reading environment variable
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_DATABASE")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN_ACCESS")