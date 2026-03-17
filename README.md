*Wat doet het script?*
- Zet \033 om naar een echte escape character (\x1b)
- Detecteert ANSI escape sequences met een regex
- Verwijdert deze sequences uit de tekst
- Geeft de opgeschoonde tekst terug

Gebruik
1. Start het script
- python3 ansi_cleaner.py
2. Voer input in
- Plak een string met ANSI escape sequences:
- test{\033[31mtest\033[39m}
3. Output
test{test}
