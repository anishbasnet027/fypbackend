# Generated by Django 4.0.1 on 2022-03-29 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0002_remove_accomodation_destination_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationTransportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation_name', models.CharField(blank=True, max_length=100)),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.destination')),
                ('transportation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.transportation')),
            ],
        ),
        migrations.CreateModel(
            name='DestinationAccomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation_name', models.CharField(blank=True, max_length=100)),
                ('accomodation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.accomodation')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.destination')),
            ],
        ),
    ]