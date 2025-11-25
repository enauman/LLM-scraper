from bs4 import BeautifulSoup
import requests
url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
item = soup.find('h1').get_text()
print(item)
items = soup.find_all('span', class_ = 'text')
for item in items:
    print(item.get_text())
