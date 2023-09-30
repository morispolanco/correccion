import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(file_path, recipient_email):
    # Configurar los detalles del correo electrónico
    sender_email = "tu_correo_electronico@gmail.com"
    sender_password = "tu_contraseña"
    subject = "Documento cargado"
    body = "Adjunto encontrarás el documento que has cargado."

    # Crear el objeto MIMEMultipart y configurar los detalles del correo electrónico
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Agregar el cuerpo del correo electrónico
    message.attach(MIMEText(body, "plain"))

    # Adjuntar el archivo al correo electrónico
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {file_path}")
        message.attach(part)

    # Enviar el correo electrónico utilizando el servidor SMTP de Gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

def main():
    st.title("Formulario de carga de documentos")

    # Mostrar el formulario para ingresar el nombre y la dirección de correo electrónico
    name = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")

    # Mostrar el formulario para cargar el documento
    uploaded_file = st.file_uploader("Cargar documento")

    if uploaded_file is not None:
        # Guardar el archivo cargado en el servidor
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Mostrar un mensaje de éxito
        st.success("El documento se ha cargado correctamente.")

        # Enviar el documento por correo electrónico
        send_email(uploaded_file.name, "mp@ufm.edu")

        # Mostrar un mensaje de éxito
        st.success("El documento se ha enviado por correo electrónico.")
