import requests
import csv
import argparse
from bs4 import BeautifulSoup

liste = []
parser = argparse.ArgumentParser(description="Scraped Buchtitel und Preise von einer Webseite")
parser.add_argument("url", nargs='?', help="Die zu durchsuchende URL")
args = parser.parse_args()
eingabe = args.url if args.url else input("Bitte geben Sie die zu durchsuchende URL ein: ")

try:
    url = requests.get(eingabe)
    url.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Fehler beim Abrufen der URL: {e}")
    exit()
url.encoding = "utf-8"
soup = BeautifulSoup(url.text, 'html.parser')
all_soups = soup.find_all("h3")
prices = soup.find_all("p", {"class": "price_color"})
if not all_soups or not prices:
    print("Keine Titel oder Preise gefunden. Diese Seite wird aktuell nicht unterstützt.")
    exit()



with open("preise.csv", "w",newline="", encoding="utf-8") as datei:
    writer = csv.writer(datei)
    writer.writerow(["Titel", "Preis"])

    for titel, preis in zip(all_soups, prices):
        print(titel.get_text(), "-", preis.get_text())
        writer.writerow([titel.get_text(), preis.get_text()])