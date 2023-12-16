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
        	password="@K2942004",
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
    
    def GetLink(self, data):
        result = self.cursor.execute(f"select * from UserPrompt;")
        # return {"payload": f'{result}'}
        result = self.cursor.fetchall()
        prompts = [item["prompt"] for item in result]

        print(prompts)
        # print(result)
        # if len(data) == 2:
        #     result = self.cur.execute(f"")
        # elif len(data) == 3:
        #     result = self.cur.execute(f"")
        
        # if len(result) > 0:
        #     return result
        # else:
        #     return make_response({"message":"Not found data"}, 204)