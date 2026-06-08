# Preisverfolger

Ein einfaches Web Scraping Tool in Python das Buchtitel und Preise von einer Website extrahiert und in eine CSV-Datei speichert.

## Live Demo

Teil des Portfolios: [monkmonk1988.github.io](https://monkmonk1988.github.io)

## Was das Tool macht

- Fragt den Nutzer nach einer URL
- Ladt die Seite und parst den HTML-Inhalt
- Extrahiert alle Titel und Preise
- Speichert die Ergebnisse in `preise.csv`
- Gibt die Ergebnisse gleichzeitig in der Konsole aus

## Voraussetzungen

```
pip install requests beautifulsoup4
```

## Nutzung

```
python preisverfolger.py
```

Dann URL eingeben, z.B.: `https://books.toscrape.com`

## Technologien

- Python 3
- requests
- BeautifulSoup4
- csv (Standardbibliothek)
