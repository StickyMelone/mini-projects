# Passwort-Generator 🔑

Ein einfacher **Passwort-Generator in Python**, der sichere Passwörter mit `secrets` erstellt.  
Das Programm stellt sicher, dass jedes Passwort mindestens einen Großbuchstaben, Kleinbuchstaben, eine Zahl und ein Sonderzeichen enthält.

---

## 🚀 Features
- Eingabe der gewünschten Passwortlänge (mindestens 4 Zeichen)
- Nutzung von `secrets` für sichere Zufallsauswahl
- Zufälliges Mischen der Zeichen für mehr Sicherheit
- Eingabeprüfung mit `try/except`
- Optionaler Debug-Modus (`DEBUG = True`)

---

## ▶️ Nutzung
```bash
python pw_generator.py


Geben Sie die gewünschte Passwortlänge ein (mindestens 4): 12
Unsortiertes Passwort: Ab1!cDe2%fGh
Generiertes Passwort: f!1Ab2%DcGhE

