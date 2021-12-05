import os.path

from django.apps import apps
from django.core import mail, serializers

from application import settings
from application.celery import app
from datetime import datetime as dt

import logging


logger = logging.getLogger(__name__)


@app.task()
def send_model_created_report(message):
    logger.info(f"New model created report with message: {message}")
    send_email(message, "New model created")
    return "Report is rent"


@app.task()
def backup_product_list(path):
    now = dt.now()
    f = open(os.path.join(path, now.strftime("%H:%M:%S-%d-%m-%Y")), "w")
    f.write(serializers.serialize('json', apps.get_model('products', 'Product').objects.all(), indent=4))
    f.close()


def send_email(message, title):
    email = mail.EmailMessage(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_RECEIVER],
    )
    email.send()
    return email
