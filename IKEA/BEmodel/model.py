from flask import make_response
from lib import app
import mysql.connector
import json
class model():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
	        host="localhost:3306",
	        user = "root",
        	password="Hieu0504@",
	        database="IKEA")
            self.mydb.autocommit = True
            self.cur = self.mydb.cursor(dictionary=True)
            print("Connect successful")
        except:
            print("ERROR!!!")

    def AddPrompt(self, data):
        self.cur.execute(f"Insert into UserPrompt(prompt) values ('{data['prompt']}')")
        return make_response({"message":"Insert successfully"}, 201)
    
    # def GetPrompt(self):
    #     result = self.cur.execute(f"SELECT * FROM UserPrompt")
    #     if len(result) > 0:
    #         return {"payload": result}
    #     else:
    #         return make_response({"message":"Not found data"}, 204)