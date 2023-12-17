from lib import app
from BEmodel.model import model
from flask import redirect, request, render_template
import googletrans
from googletrans import *
import io
from PIL import Image
import requests
from roboflow import Roboflow
import re
import json

translator = googletrans.Translator()

obj = model()

rf = Roboflow(api_key="KD6YQUhuLEnz99pUJiy5")
project = rf.workspace().project("sic-ifohb")
model = project.version(5).model

API_URL = "https://api-inference.huggingface.co/models/hatosei03/VNDH2023_Smart_Interior_Consultant_HKKTT"
headers = {"Authorization": f"Bearer {'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'}"}


def get_image_link(link):
    if ("www.ikea.com" not in link):
        return
    response = requests.get(link)
    if response.status_code == 200:
        pattern = re.compile(r'https://www.ikea.com/sa/en/images/products/.*?\.jpg')
        matches = pattern.findall(response.text)
        if matches:
            # download_image(matches[0])
            return matches[0]
        else:
            print("No image found.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

def list_class():
    prediction = model.predict("../VNDH2023-Smart-Interior-Consultant-HKKTT/IKEA/static/generated_img.jpg").json()
    products = prediction['predictions'][0]['predictions']
    res = {}
    for product in products:
        if product['confidence'] < 0.4:
            continue
        cate = product['class'].split('_')[0]
        if cate in res:
            continue
        else:
            res[cate] = product['class']
    return list(res.values())

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

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

        class_item = list_class()

        if len(class_item) > 0:
            for item in class_item:
                class_parts = item.split('_')
                url, price = obj.GetLink(class_parts)
            
            list_img = []

            for url_list in url:
                image_link = get_image_link(url_list)
                if image_link:
                    list_img.append(image_link)
            # print(list_img)
            
            list_data_json = []

            for price, url, list_img in zip(price, url, list_img):
                data_json = {
                    "url": url,
                    "link_img": list_img,
                    "price": price
                }
                list_data_json.append(data_json)

            print(json.dumps(list_data_json))
            with open("products.json", 'w') as outfile:
                json.dump(list_data_json, outfile)

    return render_template("result.html", prompt_data = data,)  