import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE

def get_connection():
    return mysql.connector.connect(
        host=HOST,
        user="root",
        password = "30052007",
        database = "signup_db"
    )