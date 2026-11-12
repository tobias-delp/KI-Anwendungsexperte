# Quellenpaket – Lokale KI im Unternehmen

**Verwendungszweck:** Gemeinsames Quellenmaterial für ChatGPT, Gamma und NotebookLM. Dieses Dokument enthält eine kurze fachliche Einführung und verweist auf überprüfbare Originalquellen. Die Unternehmensgeschichte in `01_demo_briefing_lokale_ki.md` ist fiktiv.

## 1. Was bedeutet „lokal betrieben“?

Ein lokales KI-Modell kann auf eigener Hardware oder in einer kontrollierten eigenen Infrastruktur ausgeführt werden. Ob Eingaben wirklich ausschließlich innerhalb dieser Umgebung verarbeitet werden, hängt von der **konkreten Anwendung, den aktivierten Funktionen und der Netzwerkkonfiguration** ab. „Lokal“ beschreibt zunächst den Ausführungsort und ist keine vollständige Aussage über Datenschutz oder Sicherheit.

**Frage für die Präsentation:** Welche Vorteile könnte eine kontrollierte Ausführungsumgebung für bestimmte interne Aufgaben bieten – und welche Risiken bleiben bestehen?

## 2. Was braucht der Betrieb?

Ein Betriebskonzept muss unter anderem Hardware, Modellwahl, Aktualisierungen, Zugriffsschutz, Protokollierung, Datenverwaltung, Monitoring, Fehlerbehandlung und Personalaufwand berücksichtigen. Modellgröße, Sprache, Kontextlänge, gewünschte Geschwindigkeit und gleichzeitig aktive Nutzende können den Ressourcenbedarf verändern.

**Frage:** Was müssten wir messen, bevor wir einen Vergleich zwischen lokalem Betrieb und einer freigegebenen Cloud-Lösung ziehen?

## 3. Datenschutz und Informationssicherheit

Die Verarbeitung personenbezogener Daten benötigt auch lokal eine zulässige Grundlage und geeignete Schutzmaßnahmen. Außerdem sind Rollen, Berechtigungen, Löschregeln und mögliche Anbindungen zu prüfen.

**Frage:** Welche Kontrollen verhindern, dass intern berechtigte Personen Informationen erhalten, auf die sie nicht zugreifen dürfen?

## 4. Grenzen eines Sprachmodells

Auch lokal ausgeführte Sprachmodelle können halluzinieren, Anweisungen in Dokumenten fehlinterpretieren und ungeeignete Antworten liefern. Ein Schutz durch externe Guardrails, Berechtigungskontrollen und menschliche Prüfung kann weiterhin nötig sein.

**Frage:** Welche Qualitätskriterien wären für einen Pilot überprüfbar?

## 5. Pilot statt pauschaler Empfehlung

Aus der fiktiven Ausgangslage lässt sich keine seriöse Gesamtbetriebskostenrechnung oder Erfolgsgarantie ableiten. Ein Pilot sollte zunächst ein eng eingegrenztes Anwendungsgebiet, freigegebene Testdaten, messbare Erfolgskriterien und klare Verantwortliche haben.

## Primärquellen zur Vertiefung

- Ollama-Dokumentation: https://docs.ollama.com/ – Beispiele für lokalen Modellbetrieb und dessen technische Konfiguration.
- DSGVO, konsolidierter EU-Rechtstext: https://eur-lex.europa.eu/eli/reg/2016/679/oj – datenschutzrechtliche Grundlage für personenbezogene Daten.
- OWASP GenAI Security Project: https://genai.owasp.org/ – technische Risiken von LLM-Anwendungen, darunter Prompt Injection und sensitive information disclosure.
- EU AI Act, Rechtstext: https://eur-lex.europa.eu/eli/reg/2024/1689/oj – rechtliche Pflichten für bestimmte KI-Anwendungen.

**Hinweis:** Es handelt sich um einen didaktisch zusammengestellten Überblick, keine Rechtsberatung oder konkrete Sicherheitsfreigabe. Für aktuelle Aussagen zur Implementierung bitte jeweils die Primärquelle öffnen und prüfen.
