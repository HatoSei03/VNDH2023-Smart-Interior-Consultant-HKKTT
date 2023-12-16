import requests

API_URL = "https://api-inference.huggingface.co/models/hatosei03/VNDH2023_Smart_Interior_Consultant_HKKTT"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "A modern, yellow-colored kitchen with large cupboards and a dining table",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))