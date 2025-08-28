import string
import random 
import secrets

DEBUG = False

#Zeichengruppen definieren
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation

# Alle Zeichen zusammenführen
alle_zeichen = lower + upper + digits + special
while True:
    try:
        pw_length = int(input("Geben Sie die gewünschte Passwortlänge ein (mindestens 4): "))
        if pw_length < 4:
            print("Passwortlänge muss mindestens 4 sein.")
        else:
            break
    except ValueError:
        print("Bitte eine gültige Zahl eingeben.")

# Mindestens ein Zeichen aus jeder Gruppe
pw = [
    secrets.choice(lower),
    secrets.choice(upper),
    secrets.choice(digits),
    secrets.choice(special)
]

# Restliche Zeichen zufällig auswählen
for x in range(pw_length - 4):
    zeichen = secrets.choice(alle_zeichen)
    if DEBUG:
        print(f"Runde {x}: {zeichen}")
    pw.append(zeichen)

print("Unsortiertes Passwort:", ''.join(pw))
# Passwort mischen
random.shuffle(pw)  

# Passwort in String umwandeln
password = ''.join(pw)
print("Generiertes Passwort:", password)
