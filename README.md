
# FileSegmentExtractor

Dieses Projekt sucht nach einer bestimmten Datei in einem angegebenen Ordner, extrahiert Abschnitte aus den Dateien basierend auf einem benutzerdefinierten Suchbegriff und speichert diese in einer SQLite-Datenbank sowie einer Excel-Datei.

## Funktionen

- Sucht nach einer Datei in einem angegebenen Ordner.
- Extrahiert Abschnitte aus den gefundenen Dateien basierend auf einem Suchbegriff.
- Exportiert die extrahierten Daten in eine Excel-Datei.
- Speichert die extrahierten Daten in einer SQLite-Datenbank.
- Ermöglicht das Abrufen der Daten aus der SQLite-Datenbank.

## Installation

1. Klone das Repository:

   ```bash
   git clone https://github.com/oleeeedev/FileSectionFinder.git
   ```

2. Installiere die benötigten Python-Bibliotheken:

   ```bash
   pip install pandas openpyxl
   ```

## Nutzung

1. Starte das Skript:

   ```bash
   python main.py
   ```

2. Gib den Ordnerpfad, den Dateinamen und den Suchbegriff ein, wenn du dazu aufgefordert wirst.

3. Die extrahierten Daten werden in eine Excel-Datei und in eine SQLite-Datenbank exportiert.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert.
