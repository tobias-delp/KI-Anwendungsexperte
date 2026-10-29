# Aufgaben zu Tag 4 – Daten analysieren

Alle Daten sind fiktiv. Es gibt **keine Musterlösungen** in den Teilnehmendenmaterialien. Für Aufgaben ohne Datei-Upload die betreffenden Tabellenzeilen als Text kopieren.

## Übung 1: Schulungsdaten verstehen (15 Minuten)

**Datei:** `01_schulungsdaten.csv`

1. Seht euch Spalten und Zeilen an. Was beschreibt eine Zeile?
2. Formuliert drei Fragen, die mit diesen Daten beantwortbar sein könnten.
3. Lasst euch mögliche Qualitätsprobleme nennen und belegt sie mit konkreten Zeilen.
4. Entscheidet, welche Probleme vor der Berechnung geklärt werden müssen.

## Übung 2: Zahlen und Kommentare auswerten (15 Minuten)

**Dateien:** `01_schulungsdaten.csv`, `02_schulungsfeedback.md`

1. Vergleicht die Zufriedenheit nach Schulungsthema.
2. Unterscheidet Anzahl der Antworten von Anzahl der Workshops.
3. Prüft, ob es zulässig wäre, die `workshop_kosten_eur` über sämtliche Antwortzeilen zu summieren.
4. Gruppiert die zusätzlichen Kommentare nach Themen. Belegt mindestens zwei Interpretationen mit Originalstellen.
5. Formuliert zwei Rückfragen, die für eine belastbare Entscheidung wichtig wären.

## Übung 3: Tankbelege prüfen (15 Minuten)

**Dateien:** `tankbelege/tankbeleg_001.txt` bis `_003.txt`

1. Übertragt Datum, Kraftstoffart, Liter, Literpreis und Betrag in eine einheitliche Tabelle.
2. Rechnet bei mindestens einem Beleg Menge × Preis unabhängig nach.
3. Sucht nach widersprüchlichen Angaben; kennzeichnet Unterschiede und mögliche Rundungseffekte.
4. Überlegt, was bei einem fotografierten, unscharfen Beleg zusätzlich schiefgehen könnte.

## Übung 4: Materialplanung mit Haltbarkeit (30 Minuten)

**Dateien:** `04_materialstamm.csv`, `05_lagerbestand.csv`, `06_projektplanung.csv`

1. Prüft, ob die vorhandenen Packungen alle Projekte abdecken.
2. Beachtet die **Verwendbarkeitsdauer nach Öffnung**, nicht nur die ursprüngliche Menge.
3. Bestimmt, bei welchen Projekten Material nachbestellt werden muss.
4. Ermittelt rechnerisch späteste Bestelltermine ohne Lieferpuffer.
5. Verschiebt Projekt Gamma um sieben Tage. Was verändert sich?
6. Notiert mindestens drei zusätzliche Angaben, die man in einem echten Betrieb benötigen würde.

**Für die Übung gelten diese vereinfachten Regeln:** Verbrauch erfolgt vollständig am Projektstart; Öffnungstag ist Tag 1; eine für sieben Tage nutzbare Packung ist einschließlich Öffnungstag plus sechs Tage verwendbar; vorhandene ungeöffnete Packungen werden vor neu beschafften eingesetzt, sofern sie nicht verfallen sind; Lieferzeiten sind Kalendertage; neue Packungen können rechnerisch genau am benötigten Tag eintreffen; keine Sicherheitsbestände oder Mindestbestellmengen. Pro Material werden geöffnete Restmengen mit frühestem Ablauf zuerst verbraucht.

## Übung 5: Dashboard live beobachten (15–20 Minuten)

**Programm:** `dashboard/app.py`

1. Filtert die Schulungsdaten nach einem Thema.
2. Prüft, wie sich Kennzahlen und Diagramm verändern.
3. Öffnet die Materialplanung und verändert den Verschieberegler.
4. Identifiziert eine Zahl, die erst nach Prüfung der Ausgangsdaten belastbar wäre.
5. Beschreibt, was das Dashboard **berechnet** und was es **nicht automatisch entscheidet**.

## Übung 6: Prognosen verstehen (15–20 Minuten)

**Datei:** `07_historischer_verbrauch.csv`

1. Schaut euch die Entwicklung über 36 Monate an.
2. Vergleicht eine naive Prognose (z. B. Durchschnitt der letzten drei Monate) mit späteren tatsächlichen Werten.
3. Überlegt, welche Merkmale den Verbrauch erklären könnten.
4. Warum darf ein Prognosemodell nicht mit Informationen getestet werden, die es bereits im Training gesehen hat?
5. Welche Probleme könnten bei geänderten Rahmenbedingungen auftreten?

## Reserve A: Serviceanfragen (10 Minuten)

**Datei:** `08_serviceanfragen.csv`

Ordnet Anfragen Themen und Dringlichkeiten zu, vergleicht mit den Beispielklassifikationen und diskutiert, welche Fehlzuordnungen besonders problematisch wären.

## Reserve B: Projektkapazitäten (10 Minuten)

**Datei:** `09_projektkapazitaeten.csv`

Findet zeitliche Überschneidungen und sammelt Informationen, die zur verlässlichen Kapazitätsprüfung noch fehlen (z. B. Teilzeit, tägliche Arbeitszeit, bereits eingeplante Aufgaben).

## Reserve C: Energieverbrauch (10 Minuten)

**Datei:** `10_energieverbrauch.csv`

Untersucht Tageswerte und Auffälligkeiten. Unterscheidet Beobachtung, Ursache und Vermutung.

## Reserve D: Reisekosten (10 Minuten)

**Datei:** `11_reisekosten.csv`

Erkennt fehlende Belege und mögliche Dubletten. Begründet, weshalb eine identische Betragsangabe noch keinen Betrug beweist.

## Transferfrage

Welche Datenanalyse wäre für euren Arbeitsalltag nützlich? Welche Daten wären erforderlich – und welche dürftet ihr tatsächlich verwenden?
