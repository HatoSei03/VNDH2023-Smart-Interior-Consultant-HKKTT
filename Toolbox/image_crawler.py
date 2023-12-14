import requests
import re

def download_image(image_url):
    local_filename = "../img/" + image_url.replace('https://www.ikea.com/sa/en/images/products/', '')
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
            download_image(matches[0])
            # print(matches[0])
        else:
            print("No image found.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

cnt = 0
for lines in open('data.csv', 'r').readlines():
    cnt += 1
    print(cnt)
    line = lines.split(',')
    get_image_link(line[7])
