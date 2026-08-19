import os
import smtplib
from email.message import EmailMessage
from pathlib import Path


def send_meditation(
    audio_path: Path,
    subject: str,
    body: str,
    to_email: str
):
    sender = os.environ["EMAIL_SENDER"]
    app_password = os.environ["EMAIL_APP_PASSWORD"]

    message = EmailMessage()
    message["From"] = sender
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    message.add_attachment(
        audio_path.read_bytes(),
        maintype="audio",
        subtype="wav",
        filename=audio_path.name,
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(message)
