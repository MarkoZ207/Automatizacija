# Program

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

# Funkcija za slanje emaila
def send_email(to_address, subject, body):
    from_address = "marko.maki.zlatanov@gmail.com"
    password = "your_password"  # Unesite lozinku za vaš email

    # Kreiraj email poruku
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Poveži se sa SMTP serverom i pošalji email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print(f'Email poslat na {to_address}')
    except Exception as e:
        print(f'Greška pri slanju emaila na {to_address}: {e}')

# Učitaj podatke iz Excel tabele
file_path = 'Marko.xlsx'  # Unesite putanju do vaše Excel datoteke
df = pd.read_excel(file_path)

# Pod pretpostavkom da se email adrese nalaze u koloni 'A'
email_column = 'A'
emails = df[email_column].dropna().tolist()

# Definiši niz poruka
messages = [
    "Poruka 1: Želimo vam uspešan dan!",
    "Poruka 2: Nadamo se da ste dobro.",
    "Poruka 3: Ne zaboravite na osmeh!",
    "Poruka 4: Budite produktivni!",
    "Poruka 5: Srećan rad!",
    "Poruka 6: Uživajte u svom danu.",
    "Poruka 7: Pozdrav od nas!",
    "Poruka 8: Nadamo se da uživate u radu.",
    "Poruka 9: Budite kreativni!",
    "Poruka 10: Sve najbolje!"
]

# Predmet email poruke
subject = "Dobar dan"

# Slanje emailova
for email in emails:
    # Izaberi nasumičnu poruku iz niza
    body = random.choice(messages)
    send_email(email, subject, body)
