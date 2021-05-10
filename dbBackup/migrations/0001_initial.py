# Generated by Django 3.2.2 on 2021-05-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('category', models.ManyToManyField(null=True, to='dbBackup.Category')),
            ],
        ),
    ]
