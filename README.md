# Automatizacija

import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        return

server = CustomSMTPServer(('127.0.0.1', 1025), None)
asyncore.loop()

import smtplib
from email.mime.text import MIMEText

# Postavke za Gmail SMTP server
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADRESA = "vasa@gmail.com"
LOZINKA = "vasa_lozinka"

# Povežite se sa SMTP serverom
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(EMAIL_ADRESA, LOZINKA)

# Slanje poruke
msg = MIMEText("Vaša poruka ovde")
msg["From"] = EMAIL_ADRESA
msg["To"] = "primalac@example.com"
msg["Subject"] = "Naslov poruke"
server.sendmail(EMAIL_ADRESA, "primalac@example.com", msg.as_string())

# Zatvorite vezu sa serverom
server.quit()
