# Generated by Django 3.2.2 on 2021-05-10 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbBackup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
