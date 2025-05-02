from bs4 import BeautifulSoup
from urllib import requests

url = "https://bookmeter.com/rankings"
response = request.urlopen(url)
soup = BeautifulSoup(response)
response.close()

print(soup)