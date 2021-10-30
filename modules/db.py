import os
import pymysql
import pymysql.cursors
from pymysql import Connection
from pymysql.cursors import Cursor
from dotenv import load_dotenv
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

class DB:
    def __init__(self):
        print('DB接続を開始')
        self.con: Connection = pymysql.connect(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=int(DB_PORT),
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur: Cursor = self.con.cursor()

    def __del__(self):
        print('DB接続を終了')
        self.cur.close()
        self.con.close()