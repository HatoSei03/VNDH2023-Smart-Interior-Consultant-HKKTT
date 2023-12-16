from flask import make_response
import mysql.connector
import googletrans
from googletrans import *

translator = googletrans.Translator()

class model():
    def __init__(self):
        try:
            self.connector = mysql.connector.connect(
	        host="localhost",
            port="3306",
	        user = "root",
        	password="Hieu0504@",
	        database="IKEA")
            self.cursor = self.connector.cursor(dictionary=True)
            self.connector.autocommit = True
            print("Connect successful")
        except mysql.connector.Error as e:
            print(f"ERROR!!! {e}")

    def AddPrompt(self, data):
        self.cursor.execute(f"Insert into UserPrompt(prompt) values ('{data}')")
        return make_response({"message":"Insert successfully"}, 201)
    
    # API to get prompts data from database
    def GetPrompt(self):
        result = self.cur.execute(f"SELECT * FROM UserPrompt")
        if len(result) > 0:
            return {"payload": result}
        else:
            return make_response({"message":"Not found data"}, 204)