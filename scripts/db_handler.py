import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
class DBHandler:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_book_by_title(self, title):
        query = "SELECT * FROM books WHERE title = %s"
        self.cursor.execute(query, (title,))
        return self.cursor.fetchone()
    
    def close(self):
        self.cursor.close()
        self.connection.close() 