from serpapi import GoogleSearch

params = {
  "engine": "google_reverse_image",
  "image_url": "https://www.ikea.com/sa/en/images/products/janinge-chair-yellow__0728157_pe736124_s5.jpg",
  "api_key": "7047231ed15b56d94e5aaa31bc9e894dfd9d686a9cf6071ce7396642e1358ae3"
}

search = GoogleSearch(params)
results = search.get_dict()
for result in results['inline_images']:
    # if 'www.ikea.' in result['source']:
    print(result)
        