# Generated by Django 3.1 on 2022-04-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20220409_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.client'),
        ),
    ]