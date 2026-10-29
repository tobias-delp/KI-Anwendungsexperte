# Streamlit-Dashboard – Tag 4

Ein lokales Dashboard mit drei Bereichen: Schulungsdaten, Projektmaterial mit Haltbarkeitsregeln und historische Verbrauchsprognose (Baseline und trainierte Regression). Alle Beispieldaten sind fiktiv.

## Voraussetzungen

- [uv installieren](https://docs.astral.sh/uv/getting-started/installation/)
- Python muss nicht zwingend vorher separat installiert sein; `uv` kann eine passende Python-Version bereitstellen.
- Internetverbindung bei der ersten Einrichtung zum Laden der Python-Pakete.

## Start mit uv

Öffnet ein Terminal **im Ordner `day04/dashboard`** und führt aus:

```bash
uv sync
uv run streamlit run app.py
```

Das Dashboard ist anschließend üblicherweise unter `http://localhost:8501` erreichbar. Der Terminalprozess muss dafür geöffnet bleiben; mit `Ctrl+C` beenden.

**Kein `pip` nötig.** Die Abhängigkeiten stehen in `pyproject.toml`. Optional lässt sich nach dem ersten Setup mit `uv lock` eine reproduzierbare `uv.lock` erzeugen.

## Im Kurs zeigen

1. Schulungsauswertung öffnen: Thema filtern, Datensatz und Datenqualitätsprobleme ansehen.
2. Materialplanung öffnen: Projekt Gamma verschieben und veränderten Bedarf prüfen.
3. Prognose-Demo öffnen: Monatswerte, 3-Monats-Baseline, trainierte Regression und deren Fehler vergleichen.

## Grenzen

- Kein produktionsreifes ERP-/Lagerplanungssystem.
- Keine sicheren Bestellzusagen oder echten Lieferdaten.
- Keine automatische KI-Abfrage: Die App nutzt nachvollziehbare Python-Berechnungen.
- In der Schulungsdatei ist `workshop_kosten_eur` ein Wert **pro Workshop**, obwohl er mehrfach in Antwortzeilen erscheint. Zur Kostenaggregation erst auf eindeutige Workshops reduzieren.
- CSV-Dateien mit Semikolontrennung und UTF-8-BOM.
