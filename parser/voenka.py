import requests
from bs4 import BeautifulSoup
import os

url = "https://onlinetestpad.com/zc5thdh34z2ki"
folder_name = "images"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
images = soup.find_all("img")

for img in images:
    img_url = img.attrs.get("src")
    if img_url and "http" in img_url:
        img_response = requests.get(img_url)
        img_name = img_url.split("/")[-1]
        with open(os.path.join(folder_name, img_name), "wb") as f:
            f.write(img_response.content)
            print(f"{img_name} saved")