# Preisverfolger

Ein einfaches Web Scraping Tool in Python das Buchtitel und Preise von einer Website extrahiert und in eine CSV-Datei speichert.

## Live Demo

Teil des Portfolios: [monkmonk1988.github.io](https://monkmonk1988.github.io)

## Was das Tool macht

- Lädt eine Website und parst den HTML-Inhalt
- Extrahiert alle Buchtitel und Preise (aktuell speziell für die Struktur von books.toscrape.com ausgelegt)
- Speichert die Ergebnisse in `preise.csv`
- Gibt die Ergebnisse gleichzeitig in der Konsole aus
- Fängt Netzwerkfehler und ungültige URLs ab, statt abzustürzen
- Meldet klar, wenn eine Seite keine passenden Titel/Preise enthält, statt eine leere CSV zu erzeugen

## Voraussetzungen

pip install requests beautifulsoup4

## Nutzung

Per CLI-Argument:
python preisverfolger.py https://books.toscrape.com
Oder interaktiv ohne Argument (fragt dann nach der URL):

## Technologien

- Python 3
- requests
- BeautifulSoup4
- csv (Standardbibliothek)
- argparse (Standardbibliothek)
