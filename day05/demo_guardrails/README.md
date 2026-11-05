# Optionale Guardrail-Demo

Diese Mini-Anwendung **verwendet kein Sprachmodell** und keine externen Dienste. Sie demonstriert ausschließlich einfache Schlüsselwortregeln und ihre Grenzen. **Nicht als Sicherheitsprodukt einsetzen.**

## Start mit uv

```bash
uv sync
uv run streamlit run app.py
```

## Vorführung

1. Beispiel „Normale Frage“ auswählen und die Entscheidung erklären.
2. Beispiel „Auffälliger Dokumenttext“ auswählen und die Blockierung beobachten.
3. Beispiel „Harmloser Fehlalarm“ auswählen und zeigen, dass einfache Filter zu viel sperren können.
4. Beispiel „Umformulierter Angriff“ auswählen und beobachten, dass ein schädlicher Text unter Umständen nicht erkannt wird.
5. Ein Beispiel einer Ausgangsprüfung untersuchen.

**Keine echten Personendaten, Zugangsdaten oder Unternehmensdokumente eingeben.**
