# Tag 4 – Analysieren: Von Daten zu Erkenntnissen und Prognosen

Materialpaket für den achtteiligen Kurs **„Künstliche Intelligenz in der Arbeitswelt“** (180 Minuten, Einsteigerinnen und Einsteiger). Alle Personen, Organisationen und Daten sind fiktiv.

## Inhalt

- `tag04_gamma_folien.md` – Gamma-fertige Folien, getrennt durch `---`.
- `materialien/` – Schulungsauswertung, Textfeedback, Tankbelege, MHD-/Bestellfall, historische Verbrauchswerte und vier Reservefälle.
- `uebungen/aufgabenstellungen.md` – Aufgaben ohne Lösungen.
- `dashboard/` – lokales Streamlit-Dashboard mit `uv`, siehe `dashboard/README.md`.

## Geplanter Ablauf (180 Min.)

| Zeit | Inhalt |
|---|---|
| 0–10 | Ein Rückblick auf Tag 3, Ziele |
| 10–25 | Datenanalyse, strukturierte/unstrukturierte Daten und Datenqualität |
| 25–55 | Schulungsdaten und Textfeedback |
| 55–70 | Tankbelege extrahieren und prüfen |
| 70–80 | Pause |
| 80–110 | MHD, Lager und Nachbestellung |
| 110–130 | Dashboard in Streamlit (uv) |
| 130–150 | Prognose und Machine Learning |
| 150–170 | Reservefälle oder Vertiefung |
| 170–180 | Transfer und Abschluss |

## Technik

Alle Übungen funktionieren mit Textkopien in einem normalen Chat. Für Datei-Uploads können Teilnehmer je nach verfügbaren Funktionen CSV- oder Textdateien hochladen. Keine realen Rechnungen oder vertraulichen betrieblichen Daten hochladen.

**Dashboard mit uv:**

```bash
cd day04/dashboard
uv sync
uv run streamlit run app.py
```

Die App läuft lokal. Eine Internetverbindung kann beim ersten Start für die Installation der Abhängigkeiten benötigt werden. Python-/Streamlit-Installation ist für die Teilnehmenden keine Pflicht; eine Bildschirmfreigabe der Lehrperson genügt.

## Wichtige Besonderheiten der Daten

- Schulungsdaten sind **Antwortdatensätze**, nicht Workshops. `workshop_kosten_eur` ist pro Workshop angegeben und wird in Antwortzeilen wiederholt – nicht zeilenweise summieren.
- Die Schulungsdaten enthalten absichtlich mindestens eine doppelte Antwort-ID, fehlende Zufriedenheitswerte und eine uneinheitliche Themenbezeichnung.
- Ein Tankbeleg enthält absichtlich eine Abweichung zwischen berechnetem und ausgewiesenem Betrag.
- Materialplanung basiert auf **vereinfachten, dokumentierten** Annahmen; kein echtes ERP-System und keine geprüfte Beschaffungsempfehlung.
- Der Prognose-Tab zeigt sowohl eine einfache statistische Baseline als auch eine **trainierte lineare Regression** (ältere 30 Monate Training, spätere 6 Monate Test). Beide Ansätze sind Lehrbeispiele, keine betriebsreifen Prognosen.
- Die Reservebeispiele liefern keine automatisch verbindlichen Entscheidungen.

## Quellen zur verwendeten Technik

- [uv – Projektumgebungen und `uv run`](https://docs.astral.sh/uv/guides/projects/)
- [Streamlit – Anwendung starten](https://docs.streamlit.io/develop/api-reference/cli/run)
- [Streamlit – Diagramme](https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart)
