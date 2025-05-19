# test.py
import requests

url = "http://127.0.0.1:5000/verify"
payload = {"url": "https://s.yimg.com/ny/api/res/1.2/ZIwfEA9ltPPX2eZBZhVVtA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTY0MDtoPTQyNztjZj13ZWJw/https://media.zenfs.com/en/athlon_sports_articles_610/6dc96569ae3633912ed6ef1320b64012"}
response = requests.post(url, json=payload)
print(response.json())
