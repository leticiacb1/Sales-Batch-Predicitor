import psycopg2
from .env import *

connection = psycopg2.connect(
    database=DATABASE, 
    user=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

db_cursor = connection.cursor()