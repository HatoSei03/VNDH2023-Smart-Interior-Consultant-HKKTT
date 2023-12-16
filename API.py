# 573d9065a5958541bacf2e18ca14c6e14d1e57373a4f5753915a5f476e545a424867b066b8f399fe640eaf0f500ee91f
import requests

r = requests.post('https://clipdrop-api.co/text-to-image/v1',
  files = {
      'prompt': (None, 'A brightly colored kitchen, spacious space, windows, a dining table for a family of 4, modern cooking equipment, and a luxurious cabinet system.', 'text/plain')
  },
  headers = { 'x-api-key': "4edad229deb048d1675386c72c94022b700b5adf2a577f3ac189842adb79a0c7e232df80cd73d93ab76c35677b14ecac"}
)
if (r.ok):
  # r.content contains the bytes of the returned image
    with open("result.jpg", "wb") as f:
        f.write(r.content)
    print("Vaporwave dog image downloaded successfully!")

  # 2. Optionally display the image in a GUI window:
  # This requires additional libraries like `PIL` or `cv2`.
  # import PIL.Image
  # img = PIL.Image.open("vaporwave_dog.jpg")
  # img.show()

  # 3. Access the image data for further processing:
  # You can use libraries like NumPy to work with the pixel data.
  # import numpy as np
  # image_data = np.frombuffer(r.content, dtype=np.uint8)
  # ...

#   print("Vaporwave dog image downloaded successfully!")
else:
  r.raise_for_status()