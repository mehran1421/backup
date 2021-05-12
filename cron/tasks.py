from celery import shared_task
import os
from django.core import management


@shared_task
def backup():
    management.call_command('dbbackup')