# Generated by Django 3.1 on 2022-04-25 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20220425_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='rented_to',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.client'),
        ),
    ]