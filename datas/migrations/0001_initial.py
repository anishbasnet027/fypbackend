# Generated by Django 4.0.1 on 2022-03-28 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_type', models.CharField(choices=[('T', 'Treking'), ('H', 'Hiking')], max_length=1)),
                ('destination_name', models.CharField(blank=True, max_length=100)),
                ('destination_location', models.CharField(blank=True, max_length=100)),
                ('destination_altitude', models.IntegerField(max_length=4)),
                ('destination_distance', models.IntegerField(max_length=4)),
                ('destination_avgPrice', models.IntegerField(max_length=6)),
                ('destination_equipment', models.CharField(max_length=4)),
                ('destination_emergencyContact', models.IntegerField(max_length=10)),
                ('destination_emergencyDetail', models.CharField(blank=True, max_length=100)),
                ('destination_season', models.CharField(blank=True, max_length=100)),
                ('destination_medicalNeeds', models.CharField(blank=True, max_length=100)),
                ('destination_scams', models.CharField(blank=True, max_length=100)),
                ('destination_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=40)),
                ('package_price', models.IntegerField(max_length=6)),
                ('package_provider', models.CharField(max_length=100)),
                ('package_days', models.IntegerField(max_length=2)),
                ('package_description', models.CharField(blank=True, max_length=100)),
                ('package_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='TrekGuides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_fullName', models.CharField(max_length=40)),
                ('guide_contact', models.IntegerField(max_length=10)),
                ('guide_email', models.EmailField(max_length=100)),
                ('guide_experience', models.IntegerField(max_length=2)),
                ('guide_description', models.CharField(blank=True, max_length=100)),
                ('guide_perDay_price', models.IntegerField(max_length=4)),
                ('guide_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transportation_name', models.CharField(blank=True, max_length=100)),
                ('transportation_price', models.IntegerField(max_length=4)),
                ('transportation_contact', models.IntegerField(max_length=10)),
                ('transportation_location', models.CharField(blank=True, max_length=100)),
                ('transportation_description', models.CharField(blank=True, max_length=100)),
                ('transportation_image', models.ImageField(upload_to='images')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.destination')),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation_name', models.CharField(blank=True, max_length=100)),
                ('accomodation_price', models.IntegerField(max_length=4)),
                ('accomodation_contact', models.IntegerField(max_length=10)),
                ('accomodation_location', models.CharField(blank=True, max_length=100)),
                ('accomodation_description', models.CharField(blank=True, max_length=100)),
                ('accomodation_image', models.ImageField(upload_to='images')),
                ('destination_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datas.destination')),
            ],
        ),
    ]