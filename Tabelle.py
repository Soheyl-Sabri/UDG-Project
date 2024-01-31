from tabulate import tabulate
import pandas as pd
import colorsys


table_data = [['Hauptartikelnr', 'Artikelname', 'Hersteller', 'Beschreibung', 'Materialangaben', 'Geschlecht', 'Produktart', 'Ärmel', 'Bein', 'Kragen', 'Herstellung', 'Taschenart', 'Grammatur', 'Material', 'Ursprungsland', 'Bildname']
              ['102.85', '"Paul - Mens Supersoft Organic T-Shirt"', 'Nakedshirt-Single Jersey', 'Rundhalsausschnitt mit Rippstrickbündchen, Nackenband', 'Seitennähte', 'Doppelnaht an Ärmelabschluss und Bund', 'Medium Fit', 'Neutrales Größenetikett im Nacken', '100% Bio-Baumwolle', 'Herren', 'T-Shirts;Kurzarm', 'Rundhals', '"Fair & Umweltfreundlich"', '"200 g/m²"', 'Bio-Baumwolle', '102.85.jpg']
              ['105.85', 'Coco - Womens Tank Top', 'Nakedshirt', 'Single Jersey Hals- und Armausschnitte mit Rippstrick-Einfassung', 'Seitennähte', 'Doppelnaht am Bund', 'Medium Fit', 'Neutrales Größenetikett im Nacken.', '100 % Baumwolle', 'Damen;T-Shirts;Ärmellos;;Rundhals;Fair;;"155 g/m²";Baumwolle', '105.85.jpg']
              ['106.85', '"Mia - Women\'s Organic Fitted Longtop"', 'Nakedshirt', '"Single Jersey, Decolletée und Armausschnitte mit dezenter Rippstrick-Einfassung, Seitennähte, Doppelnaht am Bund, Extra lang und körpernah geschnitten, Neutrales Größenetikett im Nacken."', '"100 % Bio-Baumwolle"', 'Damen', 'T-Shirts', 'Ärmellos', '', 'Boat-Neck', '"Fair & Umweltfreundlich"', '', '"155 g/m²"', '', '', '106.85.jpg'],
              ['107.85', '"Louise - Women\'s Fitted Top"', 'Nakedshirt', '"Single Jersey, Hals- und Armausschnitte mit Einfassung, Seitennähte, Doppelnaht am Bund, Körpernah geschnitten, Neutrales Größenetikett im Nacken. "', '"100 % Baumwolle"', 'Damen', 'T-Shirts', 'Ärmellos', '', 'Boat-Neck', '', '', '"155 g/m²"', 'Baumwolle', '', '107.85.jpg'],
              ['110.85', '"Mouse - Girl\'s Fashion T-Shirt"', 'Nakedshirt', '"Single Jersey, Rundhalsausschnitt mit Rippstrickkragen, Ärmelabschluss und Bund sind gekräuselt, Seitennähte, Neutrales Größenetikett im Nacken. "', '"100 % Baumwolle"', 'Kinder', 'T-Shirts', 'Kurzarm', '', 'Rundhals', 'Fair', '', '"155 g/m² "', 'Baumwolle', '', '110.85.jpg']
]

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

with open('table.csv', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="csv"))

df = pd.DataFrame(table_data[1:], columns=table_data[0])

html_output = df.to_html(classes='table', index=False)

with open('output.html', 'w') as f:
    f.write(f'''
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabellenoutput</title>
        <style>
            body {{
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                color: #000000;
            }}

            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }}

            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
    </body>
    </html>
    ''')

# Warum ich mich für die Skriptsprache Python entschieden habe: 
    
    # Einfach zu lernen und zu lesen: Python legt Wert auf Lesbarkeit und Einfachheit, was es besonders für Anfänger attraktiv macht.
    # Vielseitigkeit: Python wird in verschiedenen Bereichen eingesetzt, einschließlich Webentwicklung, Datenwissenschaft, künstliche Intelligenz und Automatisierung. Diese Vielseitigkeit macht es zu einer beliebten Wahl.
    # Große Community und Ressourcen: Python hat eine große und aktive Community. Es gibt eine Fülle von Ressourcen, Bibliotheken und Frameworks, die die Entwicklung unterstützen.