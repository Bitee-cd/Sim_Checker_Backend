# Generated by Django 4.1 on 2022-09-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_app', '0004_alter_phonenumber_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone_number',
            field=models.CharField(default='phone number', max_length=50),
        ),
    ]