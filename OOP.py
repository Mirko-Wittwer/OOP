# Definiert die Klasse 'Hund' als Bauplan für Hund-Objekte.
class Hund:
    # Der Konstruktor: Diese Methode wird aufgerufen, um ein neues Objekt zu erstellen.
    # 'self' repräsentiert das Objekt selbst. 'name' und 'alter' sind die übergebenen Daten.
    def __init__(self, name, alter):
        # Speichert die übergebenen Daten als Attribute (Eigenschaften) des Objekts.
        self.name = name
        self.alter = alter

    # Definiert eine Methode (Fähigkeit) der Klasse.
    def bellen(self):
        # Greift auf das 'name'-Attribut des eigenen Objekts zu und gibt einen Text aus.
        print(f"{self.name} bellt: Wuff! Wuff.")

# --- Hauptteil des Programms ---

# 1. Erstellt ein neues Objekt (eine Instanz) der Klasse 'Hund'.
# Der Konstruktor __init__ wird hier mit "bello" und 5 aufgerufen.
bello = Hund("bello", 5)

# 2. Greift auf die Attribute des 'bello'-Objekts zu und gibt sie aus.
# Der Zugriff erfolgt mit der Punkt-Notation (objekt.attribut).
print(f"Mein Hund {bello.name} ist {bello.alter} Jahre alt.")

# 3. Ruft die 'bellen'-Methode des 'bello'-Objekts auf.
# Der Aufruf erfolgt mit der Punkt-Notation und Klammern (objekt.methode()).
bello.bellen()