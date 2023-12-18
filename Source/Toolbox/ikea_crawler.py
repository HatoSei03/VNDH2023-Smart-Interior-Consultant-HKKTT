import re
import requests
import json
    
 
def download_image(image_url):
    local_filename = "../" 'fhg'+ '.jpg'
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print(f"Image successfully downloaded: {local_filename}")
    else:
        print(f"Failed to retrieve image. Status code: {response.status_code}")

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

    
keywords = ['chair', 'desk', 'wardrobes', 'bed', 'sofa', 'table', 'coffee_table', 'trolley', 'shelf']

headers = {
    'Authorization': 'Bearer 3019|jfwx2CAuSGI3twjSYyvxFATfXuBl4ZUT2z2Vos8c'
}

# for cat in keywords:
#     payload = {
#         'keyword': cat,
#         'countryCode': 'US',
#         'languageCode': 'en'
#         }
#     url = f"https://zylalabs.com/api/2226/ikea+api/2075/search+by+keyword?keyword={cat}&countryCode=US&languageCode=en"
        
#     response = requests.request("GET", url, headers=headers, data=payload)
    
#     cnt = 0
#     data = json.loads(response.text)
#     for products in data:
#         cnt += 1
#         download_image(cnt, products['image'])  

print(get_image_link('https://www.ikea.com/sa/en/p/billsbro-handle-white-20334314/'))
