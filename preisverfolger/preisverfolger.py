import requests
import csv
from bs4 import BeautifulSoup

liste = []
eingabe = input("Bitte die zu durchsuchende URL Angeben: ")
url = requests.get(eingabe)
url.encoding = "utf-8"
soup = BeautifulSoup(url.text, 'html.parser')
all_soups = soup.find_all("h3")
prices = soup.find_all("p", {"class": "price_color"})

with open("preise.csv", "w",newline="", encoding="utf-8") as datei:
    writer = csv.writer(datei)
    writer.writerow(["Titel", "Pris"])

    for titel, preis in zip(all_soups, prices):
        print(titel.get_text(), "-", preis.get_text())
        writer.writerow([titel.get_text(), preis.get_text()])