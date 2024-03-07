from promptflow import tool
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(destinatario, asunto, cuerpo, remitente, smpt, port, password):
    # create message object instance 
    msg = MIMEMultipart()
    # Configura tus credenciales SMTP y servidor
    username = remitente
    servidor = f'{smpt}:{port}'
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Adjunta el cuerpo del correo
    msg.attach(MIMEText(cuerpo, 'plain'))

   #create server 
    server = smtplib.SMTP(servidor)
    server.starttls()
    # Login Credentials for sending the mail 
    server.login(msg['From'], password)
    # send the message via the server. 
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

@tool
def echo(input: str, addressee: str, topic: str, sender: str, smpt: str, port: int, password: str) -> str:
    # Construye el cuerpo del correo según el prompt proporcionado
    cuerpo_email = input
    enviar_correo(addressee, topic, cuerpo_email, sender, smpt, port, password)

    return input