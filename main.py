from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")
print(text)
autor = soup.find_all("small", class_="author")
print(autor)
for i in range(len(text)):
    print(f"Цитата номер {i+1}")
    print(text[i].text)
    print(f"Автор цитаты - {autor[i].text}\n")

