# Generated by Django 4.1.1 on 2022-10-27 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sim_app', '0005_alter_phonenumber_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='sim_network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sim', to='sim_app.simnetwork'),
        ),
    ]
