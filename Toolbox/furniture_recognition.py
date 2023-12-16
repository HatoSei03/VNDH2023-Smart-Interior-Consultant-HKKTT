from roboflow import Roboflow

rf = Roboflow(api_key="KD6YQUhuLEnz99pUJiy5")
project = rf.workspace().project("sic-ifohb")
model = project.version(5).model

# infer on a local image
prediction = model.predict("../new_img/aeleby-swivel-armchair-gunnared-medium-grey-dark-grey__1214818_pe911748_s5.jpg").json()

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
  
print(list(res.values()))

# for product in prediction['']

# visualize your prediction
# model.predict("your_image.jpg").save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True).json())