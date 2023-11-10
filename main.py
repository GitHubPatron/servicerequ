x = input("Bitte geben Sie Ihr Jahresgehalt ein: ")
x = float(x)  # Konvertieren Sie den eingegebenen Wert in eine Gleitkommazahl (float)
y = x / 12
a = y * 0.6  # Korrekte Verwendung des Dezimalpunkts statt des Kommas
print(y)

z = input("Möchten Sie jetzt noch Ihr monatliches Nettogehalt erfahren? (Ja/Nein): ")

if z.lower() == "ja":  # Verwenden Sie lower(), um die Eingabe unabhängig von der Groß- und Kleinschreibung zu überprüfen
    print(a)
else:
    print("Alles klar, Danke für Ihre Arbeit!")