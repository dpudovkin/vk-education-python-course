from django.core import mail

from application import local_settings, settings
from application.celery import app

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


@app.task
def send_model_created_report(message):
    logger.info(f"New model created report with message: {message}")
    send_email(message, "New model created")
    return "Report is rent"


def send_email(message, title):
    email = mail.EmailMessage(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_RECEIVER],
    )
    email.send()
    return email
