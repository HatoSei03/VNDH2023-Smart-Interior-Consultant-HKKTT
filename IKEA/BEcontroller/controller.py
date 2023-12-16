from lib import app
from BEmodel.model import model
from flask import redirect, request, render_template
import googletrans
from googletrans import *

translator = googletrans.Translator()

obj = model()

@app.route('/', methods=["GET", "POST"])
def IKEA():
    return render_template("index.html")

@app.route('/onboarding', methods = ["POST"])
def onboarding():
    return render_template("onboarding.html")

@app.route('/result', methods = ["POST", "GET"])
def result():
    if request.method == 'POST':
        data = request.form.get('prompt')
        translate = translator.translate(data, dest = "en")
        new_data = translate.text
        print(new_data)
        obj.AddPrompt(new_data)
    return render_template("result.html")

     
# @app.route('/getPrompt', methods = ["GET"])
# def GetPrompt(data):
#     return obj.GetPrompt()