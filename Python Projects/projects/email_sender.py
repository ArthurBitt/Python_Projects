from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'arthurbabolat@gmail.com'
email_password = 'aalyvygagkmoubju'

email_receiver = 'bopolim435@otanhome.com'  # utilizar email do test email


assunto = "Não esqueça de praticar python"

corpo_email = """
Quando terminar de estudar, pratique!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = assunto
em.set_content(corpo_email)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
