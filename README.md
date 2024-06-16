# Automatizacija

import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


def send_email(to_address, subject, body):
    from_address = "marko.maki.zlatanov@gmail.com"
    password = "your_password"  

    
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, msg.as_string())
        server.quit()
        print(f'Email poslat na {to_address}')
    except Exception as e:
        print(f'Greška pri slanju emaila na {to_address}: {e}')


file_path = 'Marko.xlsx' 
df = pd.read_excel(file_path)


email_column = 'A'
emails = df[email_column].dropna().tolist()


messages = [
    "Želimo vam uspešan dan!",
    "Nadamo se da ste dobro.",
    "Ne zaboravite na osmeh!",
    "Budite produktivni!",
    "Srećan rad!",
    "Uživajte u svom danu.",
    "Pozdrav od nas!",
    "Nadamo se da uživate u radu.",
    "Budite kreativni!",
    "Sve najbolje!"
]

subject = "Projekat"


for email in emails:
    
    body = random.choice(messages)
    send_email(email, subject, body)
