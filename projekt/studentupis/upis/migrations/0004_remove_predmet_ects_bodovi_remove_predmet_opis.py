# Generated by Django 4.2.11 on 2024-06-10 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upis', '0003_predmet_ects_predmet_izborni_predmet_kod_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predmet',
            name='ects_bodovi',
        ),
        migrations.RemoveField(
            model_name='predmet',
            name='opis',
        ),
    ]
