import os
import pandas as pd
import sqlite3

# Excel-Datei erstellen
def export_to_excel(data, file_name):
    df = pd.DataFrame(data, columns=["Pfad", "Gefundener Abschnitt"])
    df.to_excel(file_name, index=False)
    print(f"Die Daten wurden erfolgreich in die Datei '{file_name}' exportiert.")

# Daten in die SQLite-Datenbank einfügen
def insert_into_db(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Tabelle erstellen, falls sie noch nicht existiert
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pfad TEXT,
            abschnitt TEXT
        )
    """)

    # Daten einfügen
    cursor.executemany(f"INSERT INTO {table_name} (pfad, abschnitt) VALUES (?, ?)", data)
    conn.commit()
    conn.close()
    print(f"Die Daten wurden erfolgreich in die Datenbank '{db_name}' eingefügt.")

# Daten aus der SQLite-Datenbank abfragen
def fetch_from_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    conn.close()
    return rows

# Hauptprogramm
found_files = []

while True:
    path = input("Bitte geben Sie den Pfad zum Ordner ein, wo die Datei gesucht werden soll: ")
    if os.path.exists(path):
        filename = input("Bitte geben Sie den vollständigen Dateinamen ein, nach dem gesucht werden soll: ")

        for root, dirs, files in os.walk(path):
            if filename.lower() in [f.lower() for f in files]:
                found_files.append(os.path.join(root, filename))

        if found_files:
            print(f"{len(found_files)} Datei(en) gefunden!")
            break
        else:
            print("Keine Datei gefunden!")
    else:
        print(f"Der Pfad '{path}' existiert nicht. Bitte überprüfen Sie Ihre Eingabe.")

searchterm = input("Searchterm nach dem gesucht werden soll (case sensitive): ")

extracted_data = []
for file_path in found_files:
    with open(file_path, "r") as file:
        content = file.read()

    start_element = f"<{searchterm}>"
    end_element = f"</{searchterm}>"

    try:
        start_index = content.index(start_element)
        end_index = content.index(end_element)
        segment = content[start_index:end_index + len(end_element)]
        extracted_data.append((file_path, segment))
    except ValueError:
        print(f"Kein Abschnitt mit dem Searchterm '{searchterm}' in Datei '{file_path}' gefunden.")

# Export nach Excel
excel_file = "exportierte_daten.xlsx"
export_to_excel(extracted_data, excel_file)

# In die Datenbank einfügen
db_name = "datenbank.db"
table_name = "datei_abschnitte"
insert_into_db(db_name, table_name, extracted_data)

# Daten aus der Datenbank abrufen
while True:
    user_choice = input("Möchten Sie die Daten aus der Datenbank abrufen? 1 - Ja | 2 - Nein: ")
    if user_choice == "1":
        rows = fetch_from_db(db_name, table_name)
        print("Daten aus der Datenbank:")
        for row in rows:
            print(row)
        break
    elif user_choice == "2":
        print("Programm beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte '1' oder '2' eingeben.")
