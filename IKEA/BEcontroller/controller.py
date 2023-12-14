from lib import app
from BEmodel.model import model
from flask import redirect, request, render_template

obj = model()

@app.route('/', methods=["GET", "POST"])
def IKEA():
    return render_template("index.html")

@app.route('/onboarding', methods = ["POST"])
def onboarding():
    # data = request.form.get("prompt")
    # print(data)
    # if data!=None:
    #     redirect('/result')
    return render_template("onboarding.html")

@app.route('/result', methods = ["POST"])
def result():
    data = request.form.get("prompt")
    print(data)
    return render_template("result.html")

     
# @app.route('/getPrompt', methods = ["GET"])
# def GetPrompt(data):
#     return obj.GetPrompt()