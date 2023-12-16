from lib import app
from BEmodel.model import model
from flask import redirect, request, render_template
import googletrans
from googletrans import *
import io
from PIL import Image
import requests

translator = googletrans.Translator()

obj = model()

API_URL = "https://api-inference.huggingface.co/models/hatosei03/VNDH2023_Smart_Interior_Consultant_HKKTT"
headers = {"Authorization": f"Bearer {'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'}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

image_bytes = query({"inputs": "A modern, yellow-colored kitchen with large cupboards and a dining table",})
# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))


@app.route('/', methods=["GET", "POST"])
def IKEA():
    return render_template("index.html")

@app.route('/onboarding', methods = ["POST"])
def onboarding():
    return render_template("onboarding.html")

@app.route('/result', methods = ["POST", "GET"])
def result():
    data = request.form.get('prompt')
    if request.method == 'POST':
        translate = translator.translate(data, dest = "en")
        new_data = translate.text
        obj.AddPrompt(new_data)
        image_bytes = query({"inputs":new_data,})
        print(new_data)
        # You can access the image with PIL.Image for example
        image = Image.open(io.BytesIO(image_bytes))
        image.save('IKEA/static/generated_img.jpg')
        classURL = ['bed', 'white']
        # obj.GetLink(classURL)
        print("DATATHON")
        obj.GetLink(classURL)
        # print(obj.GetLink(classURL))
    return render_template("result.html", prompt_data = data,)  

# data = json.loads(json_data)

# # Iterate through predictions
# for prediction in data.get("predictions", []):
#     # Extract class from the prediction
#     class_name = prediction.get("class", "")

#     # Split class_name based on "_"
#     class_parts = class_name.split('_')

# table_name = 'furniture'
# attribute_name = 'name'

# # Build the condition for each split part
# conditions = [f"{attribute_name} LIKE '%{part}%'" for part in split_parts]

# # Combine conditions with AND
# condition_str = " AND ".join(conditions)

# # Final SQL query
# query = f"SELECT * FROM {table_name} WHERE {condition_str};"