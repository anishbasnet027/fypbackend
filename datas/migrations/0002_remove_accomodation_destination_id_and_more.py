# Generated by Django 4.0.1 on 2022-03-29 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accomodation',
            name='destination_id',
        ),
        migrations.RemoveField(
            model_name='transportation',
            name='destination_id',
        ),
    ]
