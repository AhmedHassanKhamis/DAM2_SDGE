import smtplib
from email.message import EmailMessage

mensaje = EmailMessage()

mensaje_cuerpo = "Segunda prueba 2DAM"
usuario = "usuario"
remitente = "usuario@educa.madrid.org"
receptor = "usuario@educa.madrid.org"

cliente_smtp = "smtp01.educa.madrid.org"

mensaje['Subject'] = "2 de DAM"
mensaje['From'] = remitente
mensaje['To'] = receptor

mensaje.set_content(mensaje_cuerpo)

server = smtplib.SMTP(cliente_smtp, '587')

server.ehlo()
server.starttls()
server.login(usuario, "password")
server.send_message(mensaje)
server.quit()
