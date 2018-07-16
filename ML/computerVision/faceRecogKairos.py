import requests
import base64

# put your keys in the header
headers = {
    "app_id": "a123a233",
    "app_key": "03a5065270150ba0e23a0584ae716b0d"
}

image_string = base64.b64encode()

payload = '{"image":"capture/img1.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print r.content